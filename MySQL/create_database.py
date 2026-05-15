# Creating a Database
# To create a database in MySQL, use the "CREATE DATABASE" statement:
# create a database named "mydatabase":

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="your_user_name",
    password="your_password"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE mydatabase")


# Check if Database Exists
# You can check if a database exist by listing all databases in your system by using the "SHOW DATABASES" statement:
# Example
# Return a list of your system's databases:

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="your_user_name",
    password="your_password"
)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
  print(x)

# Try connecting to the database "mydatabase":
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="your_user_name",
  password="your_password"
  database="mydatabase"
)