# backend/database.py

from pymongo import MongoClient
from config import MONGODB_URI

client = MongoClient(MONGODB_URI)
db = client.get_database("reviewDB")
users_collection = db.get_collection("users")
reviews_collection = db.get_collection("reviews")
