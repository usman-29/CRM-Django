import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='USER',
    password='PASSWORD',
)

cursorObject = database.cursor()

cursorObject.execute("CREATE DATABASE dcrm")
print("all done!!")
