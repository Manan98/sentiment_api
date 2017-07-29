# coding: utf-8
#!/Users/mananchugh/anaconda2/bin/python
from flask import request, Blueprint
from sentiment_db import SentDB
from feature_extract import fe_pipe
import dill
from datetime import datetime
import os

sentiment_service_api = Blueprint("sentiment_service_api", __name__)
fe=''
fe = fe_pipe()
sedb = SentDB()
current_dir = os.getcwd()

@sentiment_service_api.route('/api/sentiment', methods=['POST'])
def return_score():
    time = datetime.now()
    score = get_score(get_articles(), get_processed_terms())
    current_time = datetime.now()
    result_json = {
        'article_id': get_article_id(),
        'article': get_articles(),
        'processed terms': get_processed_terms(),
        'score': get_score(),
        'time taken': (current_time - time).total_seconds()
        'type' : 'single article'
    }
    sedb.save_record(result_json)
    return score

def get_article_id():
    return (str)(request.get_json()['article_id'])

def get_articles():
    return unicode((request.get_json()['body_text'])) #.decode('utf-8')

def get_processed_terms():
    return (str)(request.get_json()['processed_terms'])

def get_score(article, pt):
    formatted = fe.transform([{'body_text':article, 'processed_terms': pt}])
    f = dill.load(file(current_dir+"/model.dill", "rb"))  # model for prediction
    score = f.predict(formatted)
    return str(score[0])
