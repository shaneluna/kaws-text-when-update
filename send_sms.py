# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = ""
auth_token = ""
client = TwilioRestClient(account_sid, auth_token)

twilioPhone = "+14083350434"

#Shane
message = client.messages.create(to="+1xxxxxxxxxx", from_=twilioPhone,
                                     body="UPDATED!!!\nhttp://kawsone.com/\n...\nGO!!")

#Rey
message2 = client.messages.create(to="+1xxxxxxxxxx", from_=twilioPhone,
                                     body="UPDATED!!!\nhttp://kawsone.com/\n...\nGO!!")
