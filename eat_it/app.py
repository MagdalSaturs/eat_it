from flask import Flask, request
from werkzeug.exceptions import HTTPException
app = Flask(__name__)

#obsługa wyjątku NotImplementedError
@app.errorhandler(NotImplementedError)
def handle_not_implemented_error(e):
    return '501 Not Implemented', 501

@app.errorhandler(HTTPException)
def handle_http_exception(e):
    return e.description, e.code
#Koniec obsługi wyjątku


@app.route('/users', methods=['GET'])
def get_users():
    return '501 Not Implemented', 501

@app.route('/users', methods=['POST'])
def create_user():
    user_data = request.get_json()
    return user_data, 201

@app.route('/users/<id>', methods=['PUT'])
def update_user(id):
    raise NotImplementedError
    user_data = request.get_json()
    return user_data, 200

@app.route('/users/<id>', methods=['PATCH'])
def partially_update_user(id):
    raise NotImplementedError
    user_data = request.get_json()
    return user_data, 200

@app.route('/users/<id>', methods=['DELETE'])
def delete_user(id):
    raise NotImplementedError
    return '', 204
