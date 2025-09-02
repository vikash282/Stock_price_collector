from pymongo import MongoClient

def get_mongo_connection():
    try:
        client = MongoClient("mongodb://localhost:27017/")
        db = client["finance_db"]
        return db
    except Exception as e:
        print(f"MongoDB connection error: {e}")
        return None
