from flask import Flask, jsonify, request
from Main import getCentroidePerCluster

app = Flask(__name__)

@app.route('/api/listCentroide', methods=['POST'])
def add_user():
    data = request.get_json() 
    response = getCentroidePerCluster(data,100,2)
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
