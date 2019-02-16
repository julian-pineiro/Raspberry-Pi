#Module: DBConnection
#Connects with the database and implements get and insert methods.
import pymysql.cursors

#CRUD EXAMPLE
passw = "V:^R|>C*.u<2M7YT0sM-8{WG1EJ_9QiT"
'''
connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com', #Must config Host.
                             user='dbmasteruser',
                             password='tK[4tH9Uw.}4',
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
'''
def insertTemp(pi, date, temp, hum):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "INSERT INTO pi"+str(pi)+" VALUES ('"+str(date)+"', '"+str(temp)+"', '"+str(hum)+"');"
            cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
     
    finally:
        connection.close()


def getStart(pi):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `start` FROM `relays` WHERE `pi_id`="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def getDuration(pi):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `duration` FROM `relays` WHERE `pi_id`="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def getDays(pi):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `days` FROM `relays` WHERE `pi_id`="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def getLastEdit(pi):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `lastedit` FROM `relays` WHERE `pi_id`="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def getAll(pi):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT * FROM `relays` WHERE `pi_id`="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def insertConfig(pi, start, minutes, days, edittime):
    try:
        connection = pymysql.connect(host='ls-e6f7569677539f634f81fad13d0e60afda8741bd.chxqoehlj9km.ap-southeast-2.rds.amazonaws.com',
                             port = 3306,   
                             user='dbmasteruser',
                             password=passw,
                             db='ojc_sensor',
                             #charset='utf8mb4'
                             #cursorclass=pymysql.cursors.DictCursor
                            )
        with connection.cursor() as cursor:
            # Create a new record
            sql = "REPLACE INTO relays VALUES ('"+str(pi)+"', '"+str(start)+"', '"+str(minutes)+"', '"+str(days)+"', '"+str(edittime)+"')"
            cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
     
    finally:
        connection.close()

