from flask import Flask, jsonify
from .config import app_config

# instantiate the app
app = Flask(__name__)

# set config
app.config.from_object(app_config.get('dev'))

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'messaage': 'Pong'
    })