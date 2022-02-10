from pymongo import MongoClient
import json
from NotificationEngine import send_SMS_Driver
def update_mongo():
    try:
        client = MongoClient('mongodb://localhost:27017/') 
    except:
        print("Could not connect to MongoDB")
    db = client.FoodDeliveryFinal
    OrderDetail = db.OrderDetail
    # def update_mongo():
    
    order_val = int(input("Please enter the Order Number for which you are facing the issue: "))
    myquery = { "Order_id": order_val }
    newvalues = { "$set": { "Complaint": "Customer is not available at the given location" } }
    OrderDetail.update_one(myquery, newvalues)

    order = OrderDetail.find({"Order_id":order_val})
    for i in OrderDetail.find({"Order_id":order_val}):
        order = i        
        if order is not None:
            send_SMS_Driver("your complaint has been registered")
            print("Your complaint has been received and is being processed. Thank you for contacting the Support.")
    
# update_mongo()