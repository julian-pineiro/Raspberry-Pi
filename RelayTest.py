'''
Assumes two relays are used and wired to BCM pin 17 and 23.
Must uncomment the rpi import and comment the fakeRPI import.

SMTP
raspberrypi.julianpineiro@gmail.com
raspberryadmin
'''
import RPi.GPIO as GPIO
#import FakeRPi.GPIO as GPIO
import time
import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import pymysql



#SMTP Configuration
sent_from = 'raspberry.julianpineiro@gmail.com'
to = 'julipineiro@gmail.com'
subject = 'Raspberry Pi Notification'
body = ''
msg = MIMEMultipart()
msg['Subject'] = subject
msg['From'] = sent_from
msg['To'] = to

#Database Configuration for temperature logging.
#db = PyMySQL.connect("localhost:port","username","password","database_name" )
#cursor = db.cursor()
#sql = "insert into table_name(id,feild1,feild2) values (1,value1,value2);"
#cursor.execute(sql)
#db.commit()


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
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)  
GPIO.cleanup()

# init list with pin numbers  
relay1 = 17
relay2 = 23
relays = [relay1, relay2]
  
# loop through pins (relays) and set mode and state to 'high'  
for i in relays:   
  GPIO.setup(i, GPIO.OUT)   
  GPIO.output(i, GPIO.HIGH)

# seconds to sleep between operations in the main loop  
SleepTimeL = 2

# main loop  
try:  
    GPIO.output(relay1, GPIO.LOW) #LOW - HIGH are both configurations of a relay.
    print ("SWITCHING ON RELAY ONE...")
    time.sleep(SleepTimeL);   
    GPIO.output(relay2, GPIO.LOW)  
    print ("SWITCHING ON RELAY TWO...")
    time.sleep(SleepTimeL);
    GPIO.output(relay1, GPIO.HIGH) #LOW - HIGH are both configurations of a relay.
    print ("SWITCHING OFF RELAY ONE...")
    time.sleep(SleepTimeL);   
    GPIO.output(relay2, GPIO.HIGH)  
    print ("SWITCHING OFF RELAY TWO...")
    time.sleep(SleepTimeL);    
    
    
# End program cleanly with keyboard  
except KeyboardInterrupt:  
    print ("Quitted")  
  
# Reset GPIO settings  
GPIO.cleanup() 
