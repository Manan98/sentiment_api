from flask import Flask, request, send_from_directory
import os
# set the project root directory as the static folder, you can set others.
app = Flask(__name__, static_url_path='')

@app.route('/api-docs/<path:path>')
def launch_swagger(path):
    file_dir = os.path.dirname(os.path.realpath(__file__))+'/api-docs'
    print("accesing path = "+file_dir+"/"+path)
    response = send_from_directory(file_dir, path)
    if '.json' in path:
        response.headers['Content-Type'] = "application/json"

    return response;

if __name__ == "__main__":
    app.run("0.0.0.0", port=5008)
