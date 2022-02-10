import sys 
sys.path.append("/mnt/c/Users/Westbrook/Documents/srh_masters/data_engineering_1/team_green/goncalo_use_case")

from pymongo import MongoClient
import json
from utils_redis import get_driver_position


client = MongoClient('mongodb://localhost:27017/')


def insert_json(collection, json_file):
    '''Inserts the given JSON file into the given collection in the FoodDelivery database'''
    with open(json_file, 'r') as file:
        data = json.load(file)
        collection.insert_many(data)


def insert_value(collection, dictionary):
    '''Inserts one row into the collection in the FoodDelivery database'''
    collection.insert_one(dictionary)


def update_value(collection, query, new_value):
    '''Updates one record in a collection'''
    collection.update_one(query, new_value)


def update_status(collection, order_id):
    '''Updates the status of the order to either delivering or completed.
    This update will trigger a function that retrieves the drivers coordinates and timestamps from the redis database.
    '''
    my_query = {'id' : order_id}
    my_order = collection.find_one({'id': order_id})
    driver_id = my_order['driver_id']

    while True:
        new_status = input(f'Update order {order_id} status:\nPress 1 for delivering\nPress 2 for completed\n')
        if new_status == str(1):
            # Update order.status
            new_value = { '$set': {'status': 'delivering'}}
            collection.update_one(my_query, new_value)
            # Update order.status_driver to delivering
            driver_data = redis_coordinates(driver_id)
            new_values = { '$set': {'status_driver.delivering': driver_data}}
            collection.update_one(my_query, new_values)

            break

        elif new_status == str(2):
            # Update order.status
            new_value = { '$set': {'status': 'completed'}}
            collection.update_one(my_query, new_value)
            # Update order.status_driver to completed
            driver_data = redis_coordinates(driver_id)
            new_values = { '$set': {'status_driver.completed': driver_data}}
            collection.update_one(my_query, new_values)

            break

        else:
            print('Invalid input! Please insert a value between 1 and 2')


def redis_coordinates(driver_id):
    '''Funcion to retrieve the drivers current position and timestamp'''
    # Get drivers name
    driver = drivers.find_one({'id': driver_id})
    driver_name = driver['first_name']
    # Get position and timestamp
    driver_coord = json.loads(get_driver_position(driver_name))
    return driver_coord


def db_setup():
    '''Setting up the database with some initial data for orders and drivers'''
    # Adding json files to collection
    files_path = '/mnt/c/Users/Westbrook/Documents/srh_masters/data_engineering_1/'
    files = {drivers:'drivers.json', orders:'orders.json'}
    for collection, file in files.items():
        insert_json(collection, files_path + file)


# Creating database
db = client.FoodDelivery

# Creating collections
orders = db.Orders
drivers = db.Drivers

if __name__ == '__main__':
    db_setup()