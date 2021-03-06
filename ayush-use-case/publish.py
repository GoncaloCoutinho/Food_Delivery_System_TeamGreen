import os
import redis
import json
import geospatialData

r = redis.Redis(charset="utf-8", decode_responses=True) # establishing redis connection

# Publishing the message on subscriber
def pub():
    time, driverName = geospatialData.calculateTime() #calling method in geoSpatial.py file to get time and driver name
    data = {
        "message": f"Your order will deliver in {time} minutes by our delivery agent {driverName}. Keep ordering from Dine Dash app to experience lightning fast delivery.",
        "from": '+18455817745',
        "to": "+4915758060202" # enter your own mobile number in order to get the SMS on your mobile.
    }
    r.publish("broadcast", json.dumps(data))

if __name__ == "__main__":
    pub()
