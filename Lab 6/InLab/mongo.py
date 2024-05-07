from pymongo import MongoClient
import pprint
import re

# client = MongoClient(host="localhost", port=27017)
client = MongoClient("mongodb://localhost:27017/")

# Get reference to 'chinook' database
db = client["chinook"]

# Get a reference to the 'customers' collection
customers_collection = db["customers"]
# print(customers_collection)

#print first document
# doc1 = customers_collection.find_one()
# print(doc1)

#print first document
doc1 = customers_collection.find_one()
print(doc1)

#return only the LastName and FirstName
for rec in customers_collection.find({},{"_id":0,"LastName": 1, "FirstName":1}):
    print(rec)

client.close()

#Print all customers with LastName that starts with “G”
rgx = re.compile('^G.*?$',re.IGNORECASE)
# compile the regex
cursor = customers_collection.find({"LastName":rgx })
num_docs = 0
for document in cursor:
    num_docs += 1
pprint.pprint(document)
print()
print("# of documents found: " + str(num_docs))

