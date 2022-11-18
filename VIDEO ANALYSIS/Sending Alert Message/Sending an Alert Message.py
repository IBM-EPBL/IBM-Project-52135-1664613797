from twilio.rest import Client


account_sid = 'AC17937b910b4774c95b3b07358838a842'
auth_token = '4b511b022adaac785f6b79b32cac4f28'
client1 = Client(account_sid, auth_token)
def sms():
    message = client1.messages \
              .create(
                  body='fire detected successfully',
                  from_='+13465214387',
                  to='+9199434 63572'
                  )
    print(message.sid)
