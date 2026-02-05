from pymongo import MongoClient
import os


MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017/")
DB_NAME = "employee_db"
COLLECTION_NAME = "employees"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
employees_col = db[COLLECTION_NAME]