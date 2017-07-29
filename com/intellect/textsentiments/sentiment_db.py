# -*- coding: utf-8 -*-
from pymongo import MongoClient
from datetime import datetime
import sentiment_service

sent_instance = sentiment_service

class SentDB:

    host = "mongodb://localhost:27017"
    client = None
    db = None
    sentiment_collection = None

    def __init__(self):
        print("############# initializing Mongo DB Client")
        self.client = MongoClient(self.host)
        self.db = self.client.infomedia_db_logs
        self.sentiment_collection = self.db.sentiment_api_logs

    def save_record(self, entry):
        entry['time of call'] = datetime.now()
        result = self.sentiment_collection.insert_one(entry)
        print(" >> record inserted successfully id = " + str(result.inserted_id))
        return str(result.inserted_id)
