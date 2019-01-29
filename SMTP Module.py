import os
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
#Needs review soon

sent_from = 'raspberrypi.julianpineiro@gmail.com'
to = 'julipineiro@gmail.com'
subject = 'Raspberry Pi Notification'
body = ''
msg = MIMEMultipart()

#Send
def notify(body_text):
    text = MIMEText(body_text)
    msg.attach(text)
    try:  
        server = smtplib.SMTP_SSL('smtp.gmail.com')
        server.ehlo()
        print("Trying to log in...\n")
        server.login('raspberrypi.julianpineiro@gmail.com', 'raspberryadmin')
        print("Logged in sucessufully!\n")
        print("Sending...\n")
        server.sendmail(sent_from, to, msg.as_string())
        server.close()
        print ('Email sent!')
    
    except:  
        print ('Check Internet Connection... Something went wrong! :(')

