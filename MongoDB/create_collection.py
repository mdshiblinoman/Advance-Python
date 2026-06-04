'''
Creating a Collection
To create a collection in MongoDB, use database object and specify the name of the collection you want to create.
MongoDB will create the collection if it does not exist.
'''
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]

mycol = mydb["customers"]

# Return a list of all collections in your database:
print(mydb.list_collection_names())

# Check if the "customers" collection exists:
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")