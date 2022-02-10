from pymongo import MongoClient
import json


client = MongoClient('mongodb://localhost:27017/')


def insert_json(collection, json_file):
    '''Inserts the given JSON file into the given collection in the FoodDelivery database'''
    with open(json_file, 'r') as file:
        data = json.load(file)
        collection.insert_many(data)


def insert_one(collection, dictionary):
    '''Inserts one row into the collection in the FoodDelivery database'''
    collection.insert_one(dictionary)


def update_one(collection, query, new_value):
    '''Updates one record in a collection'''
    collection.update_one(query, new_value)


def update_status(new_status: ['delivering', 'completed']):
    '''Updates the status of the orders collection to either delivering or completed.
    This update triggers a the status_driver to be updated with the drivers current position
    and the respective timestamp'''
    None


def update_data(collection, dictionary):
    '''Updates the row with the provided dictionary'''
    None



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