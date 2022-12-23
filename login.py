print("****Login form****")

import mysql.connector

my_database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor=my_database.cursor()

username=input("username=")
password=input("password=")

var="SELECT * FROM registration WHERE username = %s  and password = %s"
mycursor.execute(var,(username,password))
var1=mycursor.fetchone()
if var1:
    print("login succesfully")
else:
    print("invalid username or password")    
