#Module: DBConnection
#Connects with the database and implements get and insert methods.
import pymysql.cursors
passw = #password
#CRUD EXAMPLE
'''
connection = pymysql.connect(host='localhost', #Must config Host.
                             user='root',
                             password='Nosenose1234',
                             db='raspberry',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
'''
def insertTemp(pi, date, temp, hum):
    try:
        connection = pymysql.connect(host='localhost', #Must config Host.
                             user='root',
                             password=passw,
                             db='raspberry',
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
        connection = pymysql.connect(host='localhost', #Must config Host.
                             user='root',
                             password=passw,
                             db='raspberry',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `start` FROM `relays` WHERE id="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def getFinish(pi):
    try:
        connection = pymysql.connect(host='localhost', #Must config Host.
                             user='root',
                             password=passw,
                             db='raspberry',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Read a single record
            sql = "SELECT `finish` FROM `relays` WHERE id="+str(pi)
            cursor.execute(sql)
            result = cursor.fetchone()
            return result
    finally:
        connection.close()

def insertConfig(pi, start, finish):
    try:
        connection = pymysql.connect(host='localhost', #Must config Host.
                             user='root',
                             password=passw,
                             db='raspberry',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)
        with connection.cursor() as cursor:
            # Create a new record
            sql = "REPLACE INTO relays VALUES ('"+str(pi)+"', '"+str(start)+"', '"+str(finish)+"')"
            cursor.execute(sql)
            # connection is not autocommit by default. So you must commit to save
            # your changes.
            connection.commit()
     
    finally:
        connection.close()

