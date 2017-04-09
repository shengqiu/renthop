from pymongo import MongoClient
import json
import os
import sys
import operator


def insertMany(items):
  client = MongoClient('localhost', 27017)
  db = client.test_db
  collection = db.test0
  collection.insert_many(items)
  print 'there are {} of records.'.format(collection.count())
  return



if __name__ == '__main__':
  result = json.load(open('train.json', 'rb'))
  numOfRecord = len(result['listing_id'])
  colNames = result.keys()
  recordKeys = result['listing_id'].keys()
  newResult = []
  for recordKey in recordKeys:
    temp = {}
    for colName in colNames:
      temp[colName] = result[colName][recordKey]
    newResult.append(temp)
  insertMany(newResult)
  result = json.load(open('test.json', 'rb'))
  numOfRecord = len(result['listing_id'])
  colNames = result.keys()
  recordKeys = result['listing_id'].keys()
  newResult = []
  for recordKey in recordKeys:
    temp = {}
    for colName in colNames:
      temp[colName] = result[colName][recordKey]
    temp['interest_level'] = None
    newResult.append(temp)
  insertMany(newResult)
