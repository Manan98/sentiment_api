import json
from pymongo import MongoClient
from flask import Flask, request, Blueprint

sentiment_service_api = Blueprint("sentiment_service_api", __name__)

@sentiment_service_api.route('/api/sentiment', methods=['POST'])
def get_articles():
    host = "mongodb://localhost:27017"
    print("############# initializing Mongo DB Client")
    client = MongoClient(host)
    db = client.infomedia_db
    sentiment_collection = db.infomedia_articles
    a = (str)(request.get_json()['ArticleId'])
    b = (str)(request.get_json()['ProcessedTerm'])
    sentiment_cursor = sentiment_collection.find({"ArticleId": a})
    d = [field['avg_sentiment_1st_processed_term'][b] for field in sentiment_cursor]
    return json.dumps({"Score":d[0]})