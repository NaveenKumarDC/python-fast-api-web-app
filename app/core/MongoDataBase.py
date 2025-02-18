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
MONGO_USERNAME = "prd_user"
MONGO_PASSWORD = "prd_user"
MONGO_HOST = "localhost"
MONGO_PORT =27017
MONGO_DB = "prd_1"

# Create a MongoDB client
client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/{MONGO_DB};");
db = client[MONGO_DB]