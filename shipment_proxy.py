from flask import Flask, request, jsonify, Response
from flask_cors import CORS
import requests
import config
import json

app = Flask(__name__)
CORS(app)

@app.route('/shipment_proxy', methods=['POST'])
def shipment_proxy():
    if request.headers['Content-Type'] != 'application/json':
        print(request.headers['Content-Type'])
        return jsonify(res='error'), 400

    url = config.ENDPOINT
    token = config.TOKEN
    headers = {'Content-Type': 'application/json', 'Authorization': f'Bearer {token}'}
    response = requests.post(url, data=json.dumps(request.json), headers=headers)

    return jsonify(response.json()), response.status_code

if __name__ == "__main__":
    app.run(debug=True)
