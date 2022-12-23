print("*****REGISTRATION*****")

import mysql.connector

my_database=mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="mydb"
)
mycursor=my_database.cursor()

firstname=input("firstname=")
lastname=input("lastname=")
username=input("username=")
password=input("password=")
confirm_password=input("confirm password=")
email=input("email=")

var="SELECT * FROM registration WHERE username = %s"
# value_1=(username)
mycursor.execute(var,(username,))
var1=mycursor.fetchone()

if not var1:
    if(password==confirm_password):
        data="INSERT INTO registration VALUES (%s,%s,%s,%s,%s)"
        value= (firstname,lastname,username,password,email)
        mycursor.execute(data,value)
        my_database.commit()
        print("data inserted succesfully")
    else:
        print("password not matchng")    
    
else: 
    print("user already  existing")   
    

