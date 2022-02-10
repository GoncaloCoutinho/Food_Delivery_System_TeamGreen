import os
import redis
import json
import geospatialData

r = redis.Redis(charset="utf-8", decode_responses=True)

def pub():
    time, driverName = geospatialData.calculateTime()
    data = {
        "message": f"Your order will deliver in {time} minutes by our delivery agent {driverName}. Keep ordering from Dine Dash app to experience lightning fast delivery.",
        "from": '+18455817745',
        "to": "+4915758060202"
    }
    r.publish("broadcast", json.dumps(data))

if __name__ == "__main__":
    pub()