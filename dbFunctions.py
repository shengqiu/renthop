from pymongo import MongoClient
import json


def insertOne(item):
  client = MongoClient('localhost', 27017)
  db = client.test_db
  collection = db.test1
  collection.insert(item)
  print 'there are {} of records.'.format(collection.count())
  return


if __name__ == '__main__':
  result = json.load(open('test.json', 'rb'))
  numOfRecord = len(result['listing_id'])
  colNames = result.keys()
  recordKeys = result['listing_id'].keys()
  for recordKey in recordKeys:
    temp = {}
    for colName in colNames:
      temp[colName] = result[colName][recordKey]
    insertOne(temp)
