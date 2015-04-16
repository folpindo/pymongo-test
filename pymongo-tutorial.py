#!/bin/env python


import datetime
from bson.objectid import ObjectId
from pymongo import MongoClient, ASCENDING, DESCENDING
import sys
import pytz

mongo_uri = 'mongodb://localhost:27017'
database_name = 'test'
collection_name = 'test_collection'

client = MongoClient(mongo_uri)
db = client[database_name]
coll = db[collection_name]

eastern = pytz.timezone('US/Eastern')
today = datetime.datetime

data = {
    "author":"Mike",
    "text":"Blog Music Blog",
    "tags": ["rock and roll"],
    "date": today.utcnow(),
    "localized_date": eastern.localize(today.utcnow()),
    "localized_utc_date": pytz.utc.localize(today.utcnow())
}

print coll.update({"author":"Mike"}, data, True)

mike = coll.find_one({
 "author":"Mike"
})

for k,v in mike.iteritems():
 print "%s : %s" % (k,v)

sys.exit
















































"""
#mult3 = [x for x in range(1,10) if x %3 == 0]

mult3 = filter(lambda x: x%3 == 0, range(1,10))

print mult3

sys.exit
criteria = {
    '_id': ObjectId("54f968e485b6f704815850bc")
}

coll.update({"author":"Mike1"},
{
 '$set':{
  "tags":[
   "programming","python","pymongo"
  ]
 }
},
True
)
"""



sys.exit




"""
coll.insert(({
    "author":"Mike%s" % i,
    "text":"Blog %s" %i,
    "tags": ["mongodb","python","pymongo"],
    "date":datetime.datetime.utcnow()
}y) for i in xrange(10000))

sys.exit()

coll.create_index([("date", DESCENDING),("author", ASCENDING)])

index_coll = db['system_indexes']

print index_coll

indexes = index_coll.find()

print indexes.count()

sys.exit

for i in indexes:
    print i

sys.exit()

print coll.find({"author":"Mike"}).explain()["cursor"]

sys.exit()

#coll.insert(post2)ddexit

#data = coll.find(criteria)
#data = coll.find().explain()["cursor"]

data = coll.find()

#print data
#sys.exit()

for d in data:

    print "Author:", d['author']
    print "Title:", d['text']
    print "Tags:"
    for t in d['tags']:
        print "\t%s" % t
    print d['date']
"""
