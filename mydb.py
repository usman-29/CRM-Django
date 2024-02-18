import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='usman123',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE dcrm")
print("all done!!")
