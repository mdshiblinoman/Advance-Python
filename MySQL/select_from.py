# To select from a table in MySQL, use the "SELECT" statement:
# Select all records from the "customers" table, and display the result:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# To select only some of the columns in a table, use the "SELECT" statement followed by the column name(s):
mycursor.execute("SELECT name, address FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

'''
Using the fetchone() Method
If you are only interested in one row, you can use the fetchone() method.
The fetchone() method will return the first row of the result:
'''
mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchone()

print(myresult)