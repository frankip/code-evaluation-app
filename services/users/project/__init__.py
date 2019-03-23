import os
from flask import Flask, jsonify
from .config import app_config

# instantiate the app
app = Flask(__name__)


# set config
app_settings = os.getenv('APP_SETTINGS')
app.config.from_object(app_settings)


@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'messaage': 'Pong'
    })
