import utils_mongo as mongo
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Insert a new order
new_order = {
                'id': 1001,
                'client_id': 201,
                'driver_id': 0,
                'restaurant_id': 104,
                'content_id': 10394,
                'date': now,
                'status': 'preparing',
                'status_driver': {},
                'payment_total': '€70,17',
                'payment_method': 'visa'
}

mongo.insert_one(mongo.orders, new_order)

# # Updating the added order to a new time
# my_query = {'id' : 1001}
# new_values = { '$set': {'date': now}}
# mongo.update_one(mongo.orders, my_query, new_values)