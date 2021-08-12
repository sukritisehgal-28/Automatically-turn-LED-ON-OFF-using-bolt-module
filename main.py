# Light-OFF---LED-ON-
#In this project whenever the room lights gets off the led will be on automatically and will also send a sms to your phone uding twilio.
import conf
from boltiot import Sms, Bolt
import json, time

minimum_limit = 600 #you can change this accordingly
maximum_limit = 1000 #you can change this accordingly


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True: 
    print ("Reading sensor value")
    response = mybolt.analogRead('A0') 
    data = json.loads(response) 
    print("Sensor value is: " + str(data['value']))
    try: 
        sensor_value = int(data['value']) 
        if sensor_value > maximum_limit: 
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("ALERT lights are on..")
            result = mybolt.digitalWrite('1','LOW')
            print("LED is turned OFF")
        elif sensor_value < minimum_limit:
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("ALERT lights are OFF..")
            result = mybolt.digitalWrite('1','HIGH')
            print("LED is turned ON")
    except Exception as e: 
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)
