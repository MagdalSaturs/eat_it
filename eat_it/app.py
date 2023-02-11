from flask import Flask, request
app = Flask(__name__)

@app.route('/users', methods=['GET'])
def get_users():
    return '501 Not Implemented', 501

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    return user_data, 201

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    user_data = request.get_json()
    return user_data, 200

@app.route('/users/<id>', methods=['PATCH'])
def partially_update_user(id):
    user_data = request.get_json()
    return user_data, 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    return '', 204
