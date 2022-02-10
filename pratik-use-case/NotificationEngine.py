from twilio.rest import Client
import os

def send_SMS_Driver(Message):
    account_sid = os.environ['SMS_account_sid']
    auth_token = os.environ['SMS_auth_token']
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=Message, from_='+18124897545'
    , to ='+4917675605052')

def send_SMS_Customer(Message):
    account_sid = os.environ['SMS_account_sid']
    auth_token = os.environ['SMS_auth_token']
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=Message, from_='+18124897545'
    , to ='+4917675605052')