import ujson as json
from flask import Flask, request, Blueprint
import json

sentiment_service_api = Blueprint("sentiment_service_api", __name__)



@sentiment_service_api.route('/risk/article/sentiment', methods=['POST'])
def get_articles():
    print 'hi'
    return json.loads(request.form.get('ArticleId'))