# WORK IN PROGRESS ----------------
# Connection between Compass and Atlas was unsuccessful
# so I stored tables in Compass on local. 

# # API CALL for data in Atlas
# import requests
# import json

# url = "https://data.mongodb-api.com/app/data-hfhzx/endpoint/data/beta/action/findOne"

# payload = json.dumps({
#     "collection": "Orders",
#     "database": "FoodDelivery",
#     "dataSource": "Sandbox",
#     "projection": {
#     }
# })
# headers = {
#     'Content-Type': 'application/json',
#     'Access-Control-Request-Headers': '*',
#     'api-key': 'dQEFtvOKx8vTFAmpF9OK8QFJ1B1MS4be21ogoif6SIaPzwtuarMHvhkJPP4GrZn0'
# }
# response = requests.request("POST", url, headers=headers, data=payload)
# print(response.text)