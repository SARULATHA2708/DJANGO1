from pymongo import MongoClient

client = MongoClient('mongodb+srv://sarulatha315:8hB1mmfk9wYHuOZ2@pythondbcluster.srgz3py.mongodb.net/')
db = client['mydb']
users_collection = db['users']
