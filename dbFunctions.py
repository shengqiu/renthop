from pymongo import MongoClient
import json


def insertOne(item):
  client = MongoClient('localhost', 27017)
  db = client.test_db
  collection = db.test_collection
  collection.insert(item)
  for one in collection.find():
    print 'there are {} of records.'.format(len(one))
  return


if __name__ == '__main__':
  result = json.load(open('test.json', 'rb'))
  numOfRecord = len(result['listing_id'])
  colNames = result.keys()
  for i in range(numOfRecord):
    temp = {}
    for colName in colNames:
      temp[colName] = result[colName][i]
    insertOne(temp)
