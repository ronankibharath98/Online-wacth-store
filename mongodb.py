from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

uri = "mongodb+srv://ronankibharath1998:iSVXhxRLKLZf0OZV@cluster0.zd5pjbl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))

# Accessing a database using the [] notation
db = client["kalaonlinestore"]

collection = db["user_data"]