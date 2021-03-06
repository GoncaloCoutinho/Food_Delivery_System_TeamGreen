from pymongo import MongoClient
import json

#DB Connection
try:
    client = MongoClient('mongodb://localhost:27017/') 
except:
    print("Could not connect to MongoDB")

#Creating Database
db = client.FoodDeliveryFinal

#Creating Collection
CustomerDetail = db.CustomerDetail
DriverDetail = db.DriverDetail
OrderDetail = db.OrderDetail
PaymentDetails = db.PaymentDetails
TicketsDetail = db.TicketsDetail

#Dict containing object and files
collectionFileNames = {"CustomerDetail":[CustomerDetail,"CustomerDetail.json"],"DriverDetail":[DriverDetail,"DriverDetail.json"],
"OrderDetail":[OrderDetail,"OrderDetail.json"],"PaymentDetails":[PaymentDetails,"PaymentDetails.json"],"TicketsDetail":[TicketsDetail,"TicketsDetail.json"]}

#Function to insert into MongoDB
def insert_mongo():
     for _,value in collectionFileNames.items():
        # print(type(TicketsDetail))
        with open(f"{value[1]}","r") as f:
            orderList = json.load(f)
            value[0].insert_many(orderList) 

insert_mongo()