from flask import Flask, jsonify, request
from Find import find_closest_point
from Main import get_stop, getCentroidePerCluster, union

app = Flask(__name__)

@app.route('/api/listCentroide', methods=['POST'])
def listCentroide():
    data = request.get_json() 
    distance_max = 100
    min_people_per_group = 1
    response = getCentroidePerCluster(data,distance_max,min_people_per_group)
    return jsonify(response), 201

@app.route('/api/nearest_point', methods=['POST'])
def nearest_point():
    data = request.get_json() 
    response = find_closest_point(data.get("lat") , data.get("long"))
    print(response)
    return jsonify(response) , 201

@app.route('/api/plus_proche', methods=['POST'])
def plus_proche():
    data = request.get_json() 
    union(data)
    return "ok" , 201

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
