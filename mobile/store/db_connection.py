import pymongo
import pymongo.mongo_client

url = "mongodb+srv://anandbhavya92:MFgqglJC9GPgvwge@cluster0.2xt1y.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

client = pymongo.MongoClient(url)

db= client["store"]