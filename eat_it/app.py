from flask import Flask, Response
app = Flask(__name__)

@app.get('/ping')
def ping():
    return Response(status = 501)

@app.get('/users')
def users():
    return Response(status = 501)

@app.patch('/users/<user_id>')
def user(user_id):
    return Response(status = 501)

@app.post('/users')
def create_user():
    return Response(status = 501)

@app.delete('/users/<user_id>')
def delete_user(user_id):
    return Response(status = 501)

@app.put('/users/<user_id>')
def update_user(user_id):
    return Response(status = 501)

@app.get('/users')
def users():
    return Response(status = 501)

@app.post('/users')
def create_user():
    user = request.json
    return jsonify(user)

@app.put('/users/<id>')
def update_user(user_id):
    user = request.json
    return jsonify(user)

@app.patch('/users/<id>')
def user(user_id):
    user = request.json
    return jsonify(user)

@app.delete('/users/<user_id>')
def delete_user(user_id):
    return Response(status = 204)
