'''
Module: Raspberry Field
This is the raspberry pi that will be controlling the pumps.
It read its configuration from the database and acts accordingly.
By now, assumes two relays are used and wired to BCM pin 17 and 23.

Must uncomment the rpi import and comment the fakeRPI import.
'''

''' Imports '''
#import RPi.GPIO as GPIO
import FakeRPi.GPIO as GPIO
import time as t
from datetime import datetime  
from datetime import timedelta
import datetime
import Notify as mail
from HardwareModules import Relay
import Conversions as convert
import DBConnection as db

''' This Pi Configuration '''
#Pi_id is the name it will
#Have in the database.
pi_id = 2

#to turn on the board.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()

# init Relay(s) with pin numbers  
pumpRelay = Relay("Pump", 20)
pumpRelay.switchOff()

# seconds to sleep between operations in the main loop  
SleepTime = 60

#Get the data to work.

print("Getting data...")
data = db.getAll(pi_id)
start = data.get("start")
duration = int(data.get("duration"))
duration_seconds = duration*60
days = int(data.get("days"))
lastedit = data.get("lastedit")
print("Data gathered...")
starttimes = []
endtimes = []
for i in range(days):
    starttimes.append(start + timedelta(days=i))
for j in range(days):
    endtimes.append(starttimes[j] + timedelta(minutes=duration))


'''Configuration end '''


''' Main loop start '''
print("Entering main loop...")
# main loop
while True:
    now = datetime.datetime.now()
    data = db.getAll(pi_id)
    newedit = data.get("lastedit")
    newedit = convert.sql_to_datetime(str(newedit))

    #refresh the database data
    if (newedit != lastedit):
        print("Getting data...")
        start = data.get("start")
        duration = int(data.get("duration"))
        duration_seconds = duration*60
        days = int(data.get("days"))
        lastedit = data.get("lastedit")
        print("Data gathered...")
        starttimes = []
        endtimes = []
        for i in range(days):
            starttimes.append(start + timedelta(days=i))
        for j in range(days):
            endtimes.append(starttimes[j] + timedelta(minutes=duration))
        lastedit = newedit
        
    #Get the time
    #If the current time is between the start time and the finish time of any...
    for thistime in range(len(starttimes)):
        if ((now-starttimes[thistime]).total_seconds()>0 and
            (now-endtimes[thistime]).total_seconds()<0):
            #Get the total time to water.
            #Turn on the pump
            pumpRelay.switchOn()
            mail.notify("Watering valve 1")
            print("Watering Valve 1.")
            #Wait the watering time
            print("Sleeping "+str(duration)+" minutes")
            t.sleep(duration_seconds)
            #Turn off the pump
            pumpRelay.switchOff()
            print("No longer watering.")
            mail.notify("No longer watering valve 1")
            
        #Go back to checking after a while.
        print("Sleeping "+ str(SleepTime)+ " seconds.")
        t.sleep(SleepTime)
    

  
# Reset GPIO settings  
GPIO.cleanup() 
