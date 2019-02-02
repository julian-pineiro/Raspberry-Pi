#Module: DBConnection
#Connects with the database and implements get and insert methods.
import pymysql

#Database Configuration for temperature logging.
db = PyMySQL.connect("localhost:port","sensorio","vvhc*p+n)~ht","ojc_sensor" )
cursor = db.cursor()

#Example:
#sql = ""
#cursor.execute(sql)
#db.commit()
#print("Sensor 01 database created.")

def insertTempHum(date, temp, hum):
    sql = "insert into "+Temperature+"(id,feild1,feild2) values ("+date+
        ","+temp+","+hum+");"
    cursor.execute(sql)
    db.commit()

