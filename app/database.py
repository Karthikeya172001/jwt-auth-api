from pymongo import MongoClient
import os

client = MongoClient(os.getenv("MONGO_URI"))
db = client["auth_db"]
users_collection = db["users"]

