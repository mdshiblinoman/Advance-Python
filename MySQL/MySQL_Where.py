# Select record(s) where the address is "Park Lane 38": result:
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="Root@1234",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Wildcard Characters
# You can also select the records that starts, includes, or ends with a given letter or phrase.
# Use the %  to represent wildcard characters:
sql = "SELECT * FROM customers WHERE address LIKE '%way%'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# Prevent SQL Injection
# When query values are provided by the user, you should escape the values.
# This is to prevent SQL injections, which is a common web hacking technique to destroy or misuse your database.
# The mysql.connector module has methods to escape query values:
sql = "SELECT * FROM customers WHERE address = %s"
adr = ("Yellow Garden 2", )

mycursor.execute(sql, adr)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)