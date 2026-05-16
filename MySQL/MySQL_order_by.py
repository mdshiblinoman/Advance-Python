# Sort the Result
# Use the ORDER BY statement to sort the result in ascending or descending order.
# The ORDER BY keyword sorts the result ascending by default. To sort the result in descending order, use the DESC keyword.
# Sort the result alphabetically by name: result:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="12345678",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


# Sort the result reverse alphabetically by name:
sql = "SELECT * FROM customers ORDER BY name DESC"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)