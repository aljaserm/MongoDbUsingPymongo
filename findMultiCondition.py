import pymongo
from pymongo import MongoClient
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
'''
# initiate the client
client = MongoClient()
# to create or call DB
db = client.pyMongoTest
user = db.users
favNumNew= user.count_documents({"FavoriteNumber": 7, "favoriteColor":"Blue"})
print(favNumNew)