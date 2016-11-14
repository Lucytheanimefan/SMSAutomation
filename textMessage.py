from twilio.rest import TwilioRestClient
import shlex, subprocess

accountSID = 'ACfa9094405d6b559c416fd3ad8130fba5'
authToken = 'e48ef408dce62b535dec8eb72aa1fa93'
myTwilioNumber = '+17324225559'
myCellPhone = '+19082405834'

#twilioCli = TwilioRestClient(accountSID, authToken)
#message = twilioCli.messages.create(body='Let me know if you get this!', from_=myTwilioNumber, to = myCellPhone)

def text_myself(message):
    twilioCli = TwilioRestClient(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=myTwilioNumber, to=myCellPhone)

def execute():
    print("Type the message you want to text yourself: ")
    message = input()
    text_myself(message)

if __name__== '__main__':
    execute();
