import mysql.connector as con


connection = con.connect(
    host="localhost",
    user = "root",
    password = "Anant@1234",
   
    
)
print("Connection is done")

cursor = connection.cursor()


# cursor.execute("create database pythonWeekend")
# print("database is created")

cursor.execute("create table studentdata( id int , age int , name varchar(244))")
print("table is created")