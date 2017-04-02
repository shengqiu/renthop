from pymongo import MongoClient


def insertOne(item):
  client = MongoClient('localhost', 27017)
  db = client.test_db
  collection = db.test_collection
  collection.insert(item)
  for one in collection.find():
    print item
  
