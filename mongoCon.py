import pymongo

client = pymongo.MongoClient('')
db = client["data"]
shop = db["shop"]
