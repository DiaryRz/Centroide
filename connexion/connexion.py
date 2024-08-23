from pymongo import MongoClient, errors
from dotenv import load_dotenv
import os
from pymongo import MongoClient

load_dotenv()

def connexion(collectionName):
    try:
        host = os.getenv('host', 'localhost')
        port = int(os.getenv('port', 27017))
        username = os.getenv('user_')
        password = os.getenv('password')
        authSource = os.getenv('authentication-database', 'admin')
        database = os.getenv('database')
        if username and password:
            mongo_url = f"mongodb://{username}:{password}@{host}:{port}/?authSource={authSource}"
        else:
            mongo_url = f"mongodb://{host}:{port}/?authSource={authSource}"

        client = MongoClient(mongo_url)
        db = client[database]
        collection = db[str(collectionName)]
        
        return collection
    except errors.PyMongoError as e:
        print(f"Erreur avec MongoDB : {e}")

