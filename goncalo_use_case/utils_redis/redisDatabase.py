import redis
import json

if __name__ == "__main__":
    from tableDefinition import drivers, drivers_names, date_time, ini_latitude, ini_longitude
else:
    from utils_redis.tableDefinition import drivers, drivers_names, date_time, ini_latitude, ini_longitude


r = redis.Redis(db=1)


def insert_coordinates(date, longitude, latitude, driver):
    '''Insert coordinates into redis:
    Note: The date should come in the following format: '%Y-%m-%d %H:%M:%S'
    '''
    r.geoadd(name = driver, values = [longitude, latitude, date])


def insert_driver(name, id):
    '''Insert driver into redis:
    The driver id should be an int
    '''
    r.hset('drivers', name, id)


def get_driver_position(driver_name):
    '''Gets the drivers last coordinates as longitude and latitude values'''
    driver_id = r.hget('drivers', driver_name)
    date = r.zrange(driver_id, -1, -1)
    coord = r.geopos(0, *date)
    json_file = {driver_name: {'longitude': coord[0][0], 'latitude': coord[0][1], 'date': date[0].decode("utf-8")}}

    print(f'Driver {driver_name} is in longitude {coord[0][0]} and latitude {coord[0][1]}.\nUpdated at {date[0].decode("utf-8")}')

    return json.dumps(json_file, indent = 4)


def db_setup():
    counter = 0
    for driver in drivers:
        # Store the drivers with ID and name
        insert_driver(drivers_names[counter], driver)
        counter += 1
        # Store initial coordinates
        r.geoadd(driver, [ini_longitude, ini_latitude, str(date_time)])


if __name__ == "__main__":
    db_setup()
    r.bgsave()