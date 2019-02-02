'''
Assumes two relays are used and wired to BCM pin 17 and 23.
Must uncomment the rpi import and comment the fakeRPI import.
'''
#import RPi.GPIO as GPIO
import FakeRPi.GPIO as GPIO
import time
import Notify as mail
import HardwareModules as modules
    
#to turn on the board.
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()

# init list with pin numbers  
relay1 = modules.Relay("Relay 1", 17)
relay2 = modules.Relay("Relay 2", 23)

# seconds to sleep between operations in the main loop  
SleepTimeL = 2

# main loop  
try:  
    '''
    CODE
    '''
    
# End program cleanly with keyboard 
except KeyboardInterrupt:  
    print ("Quitted")  
  
# Reset GPIO settings  
GPIO.cleanup() 
