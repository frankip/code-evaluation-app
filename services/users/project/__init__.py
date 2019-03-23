from flask import Flask, jsonify

# instantiate the app
app = Flask(__name__)

@app.route('/users/ping', methods=['GET'])
def ping_pong():
    return jsonify({
        'status': 'success',
        'messaage': 'Pong'
    })