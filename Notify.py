#Module: EmailNotify
#Implements email notifications for emergency notification.
'''

SMTP
raspberrypi.julianpineiro@gmail.com
'''
import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate

#SMTP Configuration
sent_from = 'raspberry.julianpineiro@gmail.com'
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
        #print("Trying to log in...")
        server.login('raspberry.julianpineiro@gmail.com', 'password')
        #print("Logged in sucessufully!")
        #print("Sending...")
        server.sendmail(sent_from, to, msg.as_string())
        server.close()
        #print ('Email sent!')
    
    except:  
        print ('Check Internet Connection... Something went wrong! :(')

