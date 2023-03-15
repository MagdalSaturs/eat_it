from flask import Flask, Response, request, jsonify
from eat_it.controllers import AddUserController, AddUserRequest
from eat_it.controllers import GetUserController, GetUserRequest
from eat_it.controllers import PatchUserController, PatchUserRequest
from eat_it.controllers import DeleteUserController, DeleteUserRequest
from eat_it.controllers import PutUserController, PutUserRequest


app = Flask(__name__)


@app.get('/users')
def users():
    controller = GetUserController()
    get_user_request = GetUserRequest(user_id=1)
    controller.get(request=get_user_request)
    return Response(status=501)


@app.post('/users')
def create_user():
    user = request.json
    controller = AddUserController()
    add_user_request = AddUserRequest(user=user)
    controller.add(request=add_user_request)
    return jsonify(user)


@app.patch('/users/<id>')
def user(user_id):
    user = request.json
    controller = PatchUserController()
    patch_user_request = PatchUserRequest(user_id=user_id, user=user)
    controller.patch(request=patch_user_request)
    return jsonify(user)


@app.delete('/users/<user_id>')
def delete_user(user_id):
    controller = DeleteUserController()
    delete_user_request = DeleteUserRequest(user_id=user_id)
    controller.delete(request=delete_user_request)
    return Response(status=204)


@app.put('/users')
def update_user():
    user = request.json
    controller = PutUserController()
    put_user_request = PutUserRequest(user=user)
    controller.put(request=put_user_request)
    return jsonify(user)
