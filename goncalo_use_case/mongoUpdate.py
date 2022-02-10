import utils_mongo as mongo

# Updating the status from an order
mongo.update_status(mongo.orders, 1001)