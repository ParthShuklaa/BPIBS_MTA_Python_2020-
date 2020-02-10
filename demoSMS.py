import conf
from boltiot import Sms
import time
minimum_limit = 300
maximum_limit = 600
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
while True:
   try:
	   print("Making request to Twilio to send a SMS")
	   referral = "www.twilio.com/referral/NJCZHB"
	   response = sms.send_sms(f"It Works!\nHello from Twilio!\nTwilio Referral = {referral}\n-Trilok")
	   print("Hello from Twilio!\n-Trilok")
	   print("Response received from Twilio is: " + str(response))
	   print("Status of SMS at Twilio is :" + str(response.status))
   except Exception as e:
       print ("Error occured: Below are the details")
       print (e)
   time.sleep(10)