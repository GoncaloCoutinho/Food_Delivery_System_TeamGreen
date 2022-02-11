import utils_mongo as mongo
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# Insert a new order into mongodb
new_order = {
                'id': 1002,
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

mongo.insert_value(mongo.orders, new_order)