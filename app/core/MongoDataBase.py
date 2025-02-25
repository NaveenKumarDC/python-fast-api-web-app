from pymongo import MongoClient
import os
from dotenv import load_dotenv


#load environment variables
load_dotenv()

# Replace these with your MongoDB connection details
# MongoDB username
# MongoDB Password
# MongoDB hosting type
# Default port of MongoDB is 27017
# MongoDB Database name
MONGO_USERNAME = "naveendc"
MONGO_PASSWORD = "naveendc"
MONGO_HOST = "127.0.0.1"
MONGO_PORT =27017
MONGO_DB = "prd_1"

# Create a MongoDB client
# uri = f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB};"
uri = "mongodb://naveendc:naveendc@127.0.0.1:27017/?directConnection=true&serverSelectionTimeoutMS=2000&authSource=prd_1&appName=mongosh+2.3.9"
print(uri)
client = MongoClient(uri)
db = client[MONGO_DB]