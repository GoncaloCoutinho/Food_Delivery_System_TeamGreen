# Use case
In this use case I'm performing two operations, assigning the driver based on the coordinates of nearby drivers and restaurant, and then sending notification to the user of the calculated Delivery Time.

## Scheduling the Driver 
This is achieved using a Redis database that will store the longitude, latitude and name of the driver and Restaurants in the particular city. The restaurant data is fetched from the Overpass API. The Redis geospatial commands will query the nearby driver of a particular restaurant and then will assign the order to the closest driver.

## Sending out Delivery time notification
After the driver is assigned, the estimated delivery time is calculated based on driver and customer location. After calculation of Delivery time, the redis's SUB/PUB is used to send out the notification with the help of an API in the form of SMS to customer's mobile number.
