import pymongo
from pymongo import MongoClient
import datetime

'''
To connect to default client
client = MongoClient()


To connect to not default client
client = MongoClient("host",port number)
host stands for collection name. in SQL world it means database name
table == document
ex:
client = MongoClient("localhos",27017)

To connect via url:
client = MongoClient("mongodb://host:Port number")
ex:
client = MongoClient("mongodb://localhost:27018")

$gt = greater than
$lt = less than
$gte = greater than or equal
$lte = less than or equal
$eq = equal to
$ne = not equal
'''
# initiate the client
client = MongoClient()
# to create or call DB
db = client.pyMongoTest
user = db.users
currentDate = datetime.datetime.now()
oldDate = datetime.datetime(2009, 8, 11)
user1 = {"username": "MJ", "password": "MyPassword", "favoriteColor": "Blue", "FavoriteNumber": 7,
         "Hobbies": ["Coding", "TV", "Gaming"], "date": currentDate}
userId = user.insert_one(user1).inserted_id
print(user.count_documents({"date": {"$gte": oldDate}}))
print(user.count_documents({"username": {"$ne": "MJ"}}))
print(user.count_documents({"username": {"$eq": "MJ"}}))
