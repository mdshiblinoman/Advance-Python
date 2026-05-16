# You can delete an existing table by using the "DROP TABLE" statement:
# Example Get your own Python Server
# Delete the table "customers":

import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="yourusername",
  password="yourpassword",
  database="mydatabase"
)

mycursor = mydb.cursor()

sql = "DROP TABLE customers"

mycursor.execute(sql)

# If the table you want to delete is already deleted, or for any other reason does not exist, you can use the IF EXISTS keyword
# to avoid getting an error.
# Delete the table "customers" if it exists:

sql = "DROP TABLE IF EXISTS customers"

mycursor.execute(sql)