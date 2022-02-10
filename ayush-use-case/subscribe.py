import os
import redis
import json

from twilio.rest import Client
from multiprocessing import Process

r = redis.Redis(charset="utf-8", decode_responses=True) #establishing the redis connection

# Subscribing to the channel on redis server
def sub(name: str):
    pubsub = r.pubsub()
    pubsub.subscribe("broadcast") #'broadcast' is the channel name
    for message in pubsub.listen():
        if message.get("type") == "message":
            data = json.loads(message.get("data"))
            print("%s : %s" % (name, data))

            account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
            auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

            body = data.get("message")
            from_ = data.get("from")
            to = data.get("to")
            
            # Connection with Twilio for SMS sending
            client = Client(account_sid, auth_token)
            message = client.messages.create(from_=from_, to=to, body=body)
            print("message id: %s" % message.sid)


if __name__ == "__main__":
    Process(target=sub, args=("reader1",)).start() # Starts the subscribe method and listens on the server
