
from pymongo import MongoClient
from bson.json_util import dumps as bson_dumps
from bson.objectid import ObjectId
import json
from django.conf import settings

class MyMongo(object):
    def __init__(self):
        self.client = MongoClient(settings.MONGO_URL)
        self.db = self.client.mydatabase

    @staticmethod
    def find_all(collection):
        cls = MyMongo()
        obj = cls.db[collection].find({}).sort("_id", -1)
        return json.loads(bson_dumps(obj))
    
    @staticmethod
    def save(collection, data):
        cls = MyMongo()
        return cls.db[collection].insert_one(data)
    
    @staticmethod
    def delete_all(collection):
        cls = MyMongo()
        return cls.db[collection].delete_many({})
    
    @staticmethod
    def search(collection_name, min_price, max_price):
        cls = MyMongo()
        collection = cls.db[collection_name]
        query = {
            'price': {'$gte': min_price, '$lte': max_price}
        }
        return collection.find(query)