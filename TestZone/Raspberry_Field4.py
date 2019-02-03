'''
Module: Raspberry Field
This is the raspberry pi that will be deployed in the field
to gather information and store it in the database.
Assumes already working Sensors

Must uncomment the rpi import and comment the fakeRPI import.
'''

#import RPi.GPIO as GPIO
import FakeRPi.GPIO as GPIO
import time
import datetime
#import Notify as mail
import HardwareModules as modules
import DBConnection as db
import Conversions as convert

#############################
''' This Pi Configuration '''
#Pi_id is the name it will
#Have in the database.
pi_id = 4

#to turn on the board.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()

# init Temp sensor with pin number 
sensor = modules.DHT11("DHT11 Sensor",17)

# seconds to sleep between operations in the main loop  
SleepTime = 30

#Instantiate the variables
humidity = 0
temperature = 0
#############################

''' Alright, Here We Go! '''

# main loop  
while True:
    #Get sensor readings
    humidity, temperature = sensor.read()
    #Get the time and make it sql-friendly
    thistime = convert.datetime_to_sql(datetime.datetime.now())
    #Prints for testing
    #print(humidity)
    #print(temperature)
    #print(thistime)

    #Get sql statement and print it for testing
   # print("Inserting to the database...")
    db.insertTemp(pi_id,thistime,temperature,humidity)
    print("Inserted correctly: Pi number "+str(pi_id)+" values "+str(thistime)+
          ", "+str(temperature)+", "+str(humidity)+".")
    #Sleep the assigned time
    time.sleep(SleepTime)
    
  
# Reset GPIO settings  
GPIO.cleanup() 
