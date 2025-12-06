from pymongo import MongoClient

client = MongoClient(
    "mongodb+srv://karthikeya_user:Jk0j0BNBMFI4Wk7Z@karthikeya-cluster.mhzauh6.mongodb.net/?appName=karthikeya-cluster"
)

db = client["auth_db"]
users_collection = db["users"]

