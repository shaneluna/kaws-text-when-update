# /usr/bin/env python
# Download the twilio-python library from http://twilio.com/docs/libraries
from twilio.rest import TwilioRestClient

# Find these values at https://twilio.com/user/account
account_sid = "AC23649d11f4161e2f891e8e334c50115e"
auth_token = "14014f970573d3028453e7cf70181576"
client = TwilioRestClient(account_sid, auth_token)

twilioPhone = "+14083350434"

#Shane
message = client.messages.create(to="+14083093360", from_=twilioPhone,
                                     body="UPDATED!!!\nhttp://kawsone.com/\n...\nGO!!")

#Rey
message2 = client.messages.create(to="+16199485952", from_=twilioPhone,
                                     body="UPDATED!!!\nhttp://kawsone.com/\n...\nGO!!")