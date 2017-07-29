from flask import Flask, send_from_directory
import os
from com.intellect.textsentiments.sentiment_service import sentiment_service_api
from com.intellect.textsentiments.sentiment_file_service import sentiment_file_api
from flask.ext.cors import CORS

#current_dir = os.getcwd()
#UPLOAD_FOLDER = current_dir+'/com/intellect/textsentiments/files'
#ALLOWED_EXTENSIONS = set(['csv'])

app = Flask(__name__, static_url_path='')
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
cors = CORS(app, resources={r"/api/*": {"origins": "*"}})

app.register_blueprint(sentiment_file_api)
app.register_blueprint(sentiment_service_api)

@app.route('/api-docs/<path:path>')
def launch_swagger(path):
    file_dir = os.path.dirname(os.path.realpath(__file__))+'/api-docs'
    print("accessing path = "+file_dir+"/"+path)
    response = send_from_directory(file_dir, path)
    if '.json' in path:
        response.headers['Content-Type'] = "application/json"
    return response;

if __name__ == "__main__":
    app.run("0.0.0.0", port=5010)
