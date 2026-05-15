# Creating a Table
# To create a table in MySQL, use the "CREATE TABLE" statement.
# Make sure you define the name of the database when you create the connection
# Create a table named "customers":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234567890",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# Check if Table Exists
# You can check if a table exist by listing all tables in your database with the "SHOW TABLES" statement:
# Return a list of your system's databases:

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)


'''
Primary Key
When creating a table, you should also create a column with a unique key for each record.
This can be done by defining a PRIMARY KEY.
We use the statement "INT AUTO_INCREMENT PRIMARY KEY" which will insert a unique number for each record. Starting at 1, 
and increased by one for each record.
'''

mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")