from pymongo import MongoClient
import os

MONGO_URI = os.getenv("MONGO_URI", "mongodb+srv://yehuda8009_db_user:yg147741@cluster0.he6rwif.mongodb.net/")
DB_NAME = "employees_db"
COLLECTION_NAME = "employee"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
employees_col = db[COLLECTION_NAME]





