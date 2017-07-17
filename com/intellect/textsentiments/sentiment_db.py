import json
from pymongo import MongoClient
from flask import Flask, request, Blueprint

sentiment_db_api = Blueprint("sentiment_db_api", __name__)

@sentiment_db_api.route('/api/sentiment', methods=['POST'])
def get_articles():
    host = "mongodb://localhost:27017"
    print("############# initializing Mongo DB Client")
    client = MongoClient(host)
    db = client.infomedia_db_1
    sentiment_collection = db.infomedia_articles_jul_14
    id = (str)(request.get_json()['ArticleId'])
    pt = (str)(request.get_json()['ProcessedTerm'])
    sentiment_cursor = sentiment_collection.find({ "article_id": id })
    score = [field['predicted_score'] for field in sentiment_cursor if pt.lower() in (str)(field['processed_terms']).lower()]
    return json.dumps({"Score":score})