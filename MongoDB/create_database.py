'''
Creating a Database
To create a database in MongoDB, start by creating a MongoClient object, then specify a connection URL with the correct ip address and
the name of the database you want to create.
MongoDB will create the database if it does not exist, and make a connection to it.
'''
# Create a database called "mydatabase":
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# mydb = myclient["mydatabase"]

# You can check if a database exist by listing all databases in you system:
print(myclient.list_database_names())

# Or you can check a specific database by name:
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")

