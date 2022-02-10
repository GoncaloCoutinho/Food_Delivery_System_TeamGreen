from pymongo import MongoClient
import json
from NotificationEngine import send_SMS_Driver
def update_mongo():
    try:
        client = MongoClient('mongodb://localhost:27017/') #MongoDB Connection establishment
    except:
        print("Could not connect to MongoDB")
    db = client.FoodDeliveryFinal #MongoDB database creation
    OrderDetail = db.OrderDetail #MongoDB Collection creation
    # def update_mongo():
    
    order_val = int(input("Please enter the Order Number for which you are facing the issue: "))
    myquery = { "Order_id": order_val }
    newvalues = { "$set": { "Complaint": "Customer is not available at the given location" } }
    OrderDetail.update_one(myquery, newvalues) #MongoDB update_one function to update the document based on required condition

    order = OrderDetail.find({"Order_id":order_val}) #MongoDB find function to fetch required documents from collection.
    for i in OrderDetail.find({"Order_id":order_val}):
        order = i        
        if order is not None:
            send_SMS_Driver("your complaint has been registered")
            print("Your complaint has been received and is being processed. Thank you for contacting the Support.")
    
# update_mongo()