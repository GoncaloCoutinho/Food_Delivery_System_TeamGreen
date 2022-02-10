import overpass
import redis
import csv

r = redis.Redis(port=6379)
api = overpass.API()
    
#Query to get geospatial data from OpenStreetMap
query = """
area[name="Mannheim"]->.a;
( node(area.a)[amenity=restaurant];
  way(area.a)[amenity=restaurant];
  rel(area.a)[amenity=restaurant];);
"""
fmt = 'csv(::id,::lat,::lon,"name")'
data = api.get(query, responseformat=fmt)
deletedHeader = data.pop(0)
#print(data[:5])

with open('Driver_data.csv', newline='') as f:
    reader = csv.reader(f)
    driverData = list(reader)
    driverData.pop(0)

#print(driverData)

# Add driver location data in Redis Database
for driverLocation in driverData :
    try:
        if(not driverLocation[4] or not driverLocation[3] or not driverLocation[1]):
            print(f"empty {driverLocation[4]} {driverLocation[3]} {driverLocation[1]}")
        else:
            r.geoadd("driver_location",float(driverLocation[4]),float(driverLocation[3]),driverLocation[1])
    except ValueError as e:
        print (f"error {e} at {driverLocation}")

# Add restaurant location data in Redis Database
for location in data :
    try:
        if(not location[2] or not location [1] or not location[3]):
            print(f"empty {location[2]} {location[1]} {location[3]}")
        else:
            r.geoadd("location",float(location[2]),float(location[1]),location[3])
    except ValueError as e:
        print (f"error {e} at {location}")

# Get drivers within a 1km radius around restaurant
def getDrivers(restName):
    restCoor = r.geopos("location", restName)
    loc = r.georadius("driver_location",restCoor[0][0],restCoor[0][1],1,unit="km",withcoord=True, withdist=True, sort="ASC")
    return loc

def assignDriver():
    drivers = getDrivers("Estragon")
    if (drivers[0][1] == 0.0):
        drivers.pop(0)
    assignedDriver = drivers[0] 
    return assignedDriver

def calculateTime():
    assignedDriver = assignDriver()
    driverName = assignedDriver[0].decode()
    distance = assignedDriver[1]
    speed=20
    time = distance*speed
    print(time)
    return time, driverName

#calculateTime()
 
