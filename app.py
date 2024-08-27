from flask import Flask, jsonify, request
from Main import get_stop, getCentroidePerCluster

app = Flask(__name__)

@app.route('/api/listCentroide', methods=['POST'])
def listCentroide():
    data = request.get_json() 
    distance_max = 100
    min_people_per_group = 1
    response = getCentroidePerCluster(data,distance_max,min_people_per_group)
    return jsonify(response), 201

@app.route('/api/plus_proche', methods=['POST'])
def plus_proche():
    data = request.get_json() 
    rep = get_stop(data)
    return jsonify(rep) , 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
