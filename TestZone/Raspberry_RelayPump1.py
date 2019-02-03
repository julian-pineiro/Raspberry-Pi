'''
Module: Raspberry Field
This is the raspberry pi that will be controlling the pumps.
It read its configuration from the database and acts accordingly.
By now, assumes two relays are used and wired to BCM pin 17 and 23.

Must uncomment the rpi import and comment the fakeRPI import.
'''
#import RPi.GPIO as GPIO
import FakeRPi.GPIO as GPIO
import time
import datetime
#import Notify as mail
from HardwareModules import Relay
import Conversions as convert
import DBConnection as db

#############################
''' This Pi Configuration '''
#Pi_id is the name it will
#Have in the database.
pi_id = 1

#to turn on the board.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()

# init Relay(s) with pin numbers  
pumpRelay = Relay("Water Pump", 17)
pumpRelay.switchOff()

# seconds to sleep between operations in the main loop  
SleepTime = 60

#Hardcoded start times for testing.
startraw = '2019-02-03 19:45:00'
finishraw = '2019-02-03 20:00:00'
#And make them Python Friendly
#start = convert.sql_to_datetime(startraw)
#finish = convert.sql_to_datetime(finishraw)
#############################

#Provisional DB time addition
db.insertConfig(pi_id,startraw,finishraw)


''' Alright, Here We Go! '''

# main loop
while True:
    #Fetch values from database
    start = db.getStart(pi_id)
    finish = db.getFinish(pi_id)
    #Get the datetime from the dictionary returned
    start = start.get("start")
    finish = finish.get("finish")
    #Format as datetime correctly
    start = convert.sql_to_datetime(str(start))
    finish = convert.sql_to_datetime(str(finish))
    #pumpRelay.toString()
    #Get the time
    now = datetime.datetime.now()
    #If the current time is between the start time and the finish time...
    if ((now-start).total_seconds()>0 and (now-finish).total_seconds()<0):
        #Get the total time to water.
        
        countdown = (finish-start).total_seconds()
        #Turn on the pump
        pumpRelay.switchOn()
        print("Watering Pump 1.")
        #Wait the watering time
        time.sleep(countdown)
        #Turn off the pump
        pumpRelay.switchOff()
        print("No longer watering.")
        
    #Go back to checking after a while.
    time.sleep(SleepTime)
      
# Reset GPIO settings  
GPIO.cleanup() 
