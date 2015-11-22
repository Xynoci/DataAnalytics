# mkdir c:\data\db
# pip install --upgrade pymongo
# cd C:\Program Files\MongoDB\Server\3.0\bin
# run mongod
# http://api.mongodb.org/python/current/tutorial.html

import pymongo
import datetime
c = pymongo.MongoClient("localhost", 27017)

# create document
post = {"author": "Mike",
"text": "My first blog post!",
"tags": ["mongodb", "python", "pymongo"],
"date": datetime.datetime.utcnow()}
#insert document
db = c.test_database
posts = db.posts
post_id = posts.insert_one(post).inserted_id
post_id

# search database for 1 entry
posts.find_one()

# add mulitple entries
new_posts = [{"author": "Mike",
"text": "Another post!",
"tags": ["bulk", "insert"],
"date": datetime.datetime(2009, 11, 12, 11, 14)},
{"author": "Eliot",
"title": "MongoDB is fun",
"text": "and pretty easy too!",
"date": datetime.datetime(2009, 11, 10, 10, 45)}]
result = posts.insert_many(new_posts)
print result.inserted_ids
# search table
for p in posts.find():
 print p 
 
# search specific
for p in posts.find({"author": "Mike"}):
 print p
