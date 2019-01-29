'''
Assumes two relays are used and wired to BCM pin 17 and 23.
Must uncomment the rpi import and comment the fakeRPI import.

SMTP
raspberrypi.julianpineiro@gmail.com
raspberryadmin
'''
#import RPi.GPIO as GPIO
import FakeRPi.GPIO as GPIO
import time
import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

#SMTP Configuration
sent_from = 'raspberrypi.julianpineiro@gmail.com'
to = 'julipineiro@gmail.com'
subject = 'Raspberry Pi Notification'
body = ''
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sent_from
msg['To'] = to

#Send email function.
def notify(body_text):
    text = MIMEText(body_text)
    msg.attach(text)
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        print("Trying to log in...")
        server.login('raspberry.julianpineiro@gmail.com', 'raspberrypass')
        print("Logged in sucessufully!")
        print("Sending...")
        server.sendmail(sent_from, to, msg.as_string())
        server.close()
        print ('Email sent!')
    
    except:  
        print ('Check Internet Connection... Something went wrong! :(')


#to turn on the board.
#GPIO.setmode(GPIO.BOARD)
GPIO.setmode(GPIO.BCM)  
  
# init list with pin numbers  
  
pinList = [17, 23]  
  
# loop through pins and set mode and state to 'low'  
  
for i in pinList:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH)  
  
# time to sleep between operations in the main loop  
SleepTimeL = 2  
  
# main loop  
try:  
    GPIO.output(17, GPIO.LOW) #LOW - HIGH are both configurations of a relay.
    print ("SWITCHING RELAY ONE...")
    time.sleep(SleepTimeL);   
    GPIO.output(23, GPIO.LOW)  
    print ("SWITCHING RELAY TWO...")
    time.sleep(SleepTimeL);    
    GPIO.cleanup()
    notify("Success! Relay should've switched.") 
    
# End program cleanly with keyboard  
except KeyboardInterrupt:  
    print ("Quitted")  
  
# Reset GPIO settings  
GPIO.cleanup() 
