from flask import Flask, request, send_from_directory
import os
from com.intellect.textsentiments.sentiment_db import sentiment_db_api
#from com.intellect.textsentiments.sentiment_service import sentiment_service_api
from flask.ext.cors import CORS

# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})


app.register_blueprint(sentiment_db_api)
#app.register_blueprint(sentiment_service_api)

@app.route('/api-docs/<path:path>')
def launch_swagger(path):
    file_dir = os.path.dirname(os.path.realpath(__file__))+'/api-docs'
    print("accessing path = "+file_dir+"/"+path)
    response = send_from_directory(file_dir, path)
    if '.json' in path:
        response.headers['Content-Type'] = "application/json"
    return response;

if __name__ == "__main__":
    app.run("0.0.0.0", port=5008)
