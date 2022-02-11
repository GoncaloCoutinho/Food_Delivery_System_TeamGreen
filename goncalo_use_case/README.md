# Use case
In this use case I'm performing two operations, storing gps coordinates regularly and then inserting them in a permanent storage with each order status update.

## Storing GPS coordinates
The first part of my use case is to store GPS coordinates from the drivers. This is achieved using a Redis database that will store the longitude, latitude and timestamp of the driver each 5 seconds. The costumer can then get the drivers position. Internally redis will fetch the last inserted coordinates for the driver.

## Handling status updates
Each time an order status changes there is a call to redis to retrieve the last timestamp and position of the driver assigned to the order. When an order is received the initial status is 'preparing'. When the restaurant manager changes this status to 'delivering', mongodb will store the drivers information from redis in the orders collection. When the status is changed again to 'completed' the process runs again. In the end we have two distinct references stored in the orders collection and can then calculate the time-to-delivery for each order.

## Files
* utils_mongo -> initializes the mongodb database, inserts some initial data;
* utils_redis -> initializes the redis database, inserts some initial data;
* commands.txt -> some redis commands for terminal, can be ignored;
* driverPosition.py -> returns the drivers current position (via redis);
* insertData.py -> inserting new drivers coordinates into redis;
* mongoInsert.py -> inserting new orders into mongodb;
* mongoUpdate.py -> update the status of the order, triggers a function that fetches the current position of the assigned driver and stores it into mongodb.