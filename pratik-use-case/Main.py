from DB_UPDATE import update_mongo
from DB_Mongo_Redis import mongoRedis
#Python file that imports all other files
print("Chose your Profile")
print("1 Driver")
print("2 Support Executive")

choise = int(input())

if choise == 1:
    print("welcome to complaint Portal")
    print("Please select the complaint category")
    print("1 the customer is not available at given location")
    choise = int(input())
    if choise == 1:
        update_mongo()

if choise == 2:
    print("welcome to Support Tools")
    print("Please select the required tool")
    print("1 Location comparision of Driver and Customer")
    choise = int(input())
    if choise == 1:
        mongoRedis()