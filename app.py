from flask import Flask, jsonify, request
from Main import getCentroidePerCluster

app = Flask(__name__)

coordinates = [
    (40.7128, -74.0060),
    (48.8566, 2.3522),  
    (40.7127, -74.0059),
    (48.8567, 2.3523),
    (-18.859335, 47.510035),
    (-18.862061, 47.511425),
    (40.7130, -74.0065),
    (48.8570, 2.3530),
    (-18.862438, 47.508311)
]

# Route pour ajouter un nouvel utilisateur
@app.route('/api/listCentroide', methods=['POST'])
def add_user():
    data = request.get_json() 
    response = getCentroidePerCluster(data,100,2)
    print(response)
    # return response, 201
    return jsonify(response), 201

if __name__ == '__main__':
    app.run(debug=True)
