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
print(client)
# to create or call DB
db = client.pyMongoTest
user = db.users

user1={"username": "MJ", "password": "MyPassword", "favoriteColor": "Blue", "FavoriteNumber": 7,
         "Hobbies": ["Coding", "TV", "Gaming"]}
userId=user.insert_one(user1).inserted_id

userObject = {"username": "KP", "password": "kpMyPassword", "favoriteColor": "Green", "FavoriteNumber": 92,
         "Hobbies": ["Coding", "TV", "Gaming"]}
userId=user.insert_one(userObject).inserted_id