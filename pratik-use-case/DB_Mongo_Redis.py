import time
from pymongo import MongoClient
import redis
from NotificationEngine import send_SMS_Driver, send_SMS_Customer

def mongoRedis():
    #Redis connection
    r = redis.Redis(host='localhost', port=6379, db=0)
    drivers_location = [49.41325445,7.6559615]
    #redis geoadd fucntion
    r.geoadd("Location",[drivers_location[0],drivers_location[1],"Driver"])
    #mongo connection establishment
    try:
        client = MongoClient('mongodb://localhost:27017/') 
    except:
        print("Could not connect to MongoDB")
    db = client.FoodDeliveryFinal
    OrderDetail = db.OrderDetail
    order_val = int(input("Please enter the order number for which location has to be compared: "))
    #MongoDB find_one funtion to find the record based on condition
    order = OrderDetail.find_one({"Order_id":order_val})
    # for i in OrderDetail.find_one({},{"Order_id":order}):
    # a = OrderDetail.find_one({"Order_id":order})
    mylist = []
    mylist.append(order["Order_longitude"])
    mylist.append(order["Order_latitude"])
    r.geoadd("Location",[mylist[0],mylist[1],"Customer"])
    #Redis geodist function to measure the distance between two locations
    dist = r.geodist(name = "Location",place1 = "Customer", place2 = "Driver",unit = 'm')
    # print(dist)
    if dist == 0.0:
        r.set("expire","waitingTime")#Redis Set fucntion to set a key value pair
        r.expire("expire",3)#Redis Expire function used to set expiry of a key
        #Redis ttl fucntion to check the time to live of the expire key
        while(r.ttl("expire")>=1):
            if r.ttl("expire") == 1:
                time.sleep(2)
                print("Thanks for your patience. It looks like the customer is not available at the given location")
                send_SMS_Driver("Your complaint has been taken care of. The order can be canceled.")
                time.sleep(2)
                send_SMS_Customer("Your order was canceled because you were unavailable at the specified location.")
                print("Customer and Driver have been notified.")
                break
    else:
        print("Thanks for your patience. It looks like the Driver is far from customer location. The driver has been notified")
        send_SMS_Driver("you are not in the correct location. please navigate to correct location")
                