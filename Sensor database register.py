import time
import RPi.GPIO as GPIO
import datetime
import Adafruit_DHT as sensor
import pymysql

'''  
Temperature sensor config
Positive on pin 1
Ground on pin 6
Data on pin 11 (GPIO 17)
'''

#Actual code is commented until the database table is created.

#Database Configuration for temperature logging.
db = PyMySQL.connect("localhost:port","sensorio","vvhc*p+n)~ht","ojc_sensor" )
cursor = db.cursor()
#sql = "insert into table_name(id,feild1,feild2) values (1,value1,value2);"
sql = "CREATE TABLE `ojc_sensor`.`sensor01` (`time` DATETIME NOT NULL,`temperature` DECIMAL(4,1) NULL,`humidity` DECIMAL(4,1) NULL,PRIMARY KEY (`time`),UNIQUE INDEX `time_UNIQUE` (`time` ASC) VISIBLE);"

cursor.execute(sql)
db.commit()
print("Sensor 01 database created.")

'''
while True:
    #Read_retry Parameters are (model, GPIO data port)
    humidity, temperature = sensor.read_retry(11,17)
'''  
