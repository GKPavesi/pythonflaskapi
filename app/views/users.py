from werkzeug.security import generate_password_hash
from app import db
from flask import request, jsonify
from ..models.users import Users, user_schema, users_schema

def post_user():
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    pass_hash = generate_password_hash(password)
    user = Users(username, pass_hash, name, email)

    try:
        db.session.add(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "successfully registered", "data": result}), 201
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return jsonify({"message": "unable to create", "data": {}}), 500
    
def update_user(id):
    username = request.json['username']
    password = request.json['password']
    name = request.json['name']
    email = request.json['email']

    user = Users.query.get(id)

    if not user:
        return jsonify({"message": "user doesn't exists", "data": {}}), 404
    
    pass_hash = generate_password_hash(password)

    try:
        user.username = username
        user.password = pass_hash
        user.name = name
        user.email = email
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "successfully updated", "data": result}), 201
    except Exception as e:
        return jsonify({"message": "unable to update", "data": {}}), 500
    
def get_users():

    users = Users.query.all()
    if users:
        result = users_schema.dump(users)
        return jsonify({"message": "successfully fetched", "data": result}), 200
    
    return jsonify({"message": "no users found", "data": {}}), 404

def get_user(id):

    user = Users.query.get(id)
    if user:
        result = user_schema.dump(user)
        return jsonify({"message": "successfully fetched", "data": result}), 200
    
    return jsonify({"message": "users doesn't exists", "data": {}}), 404

def delete_user(id):

    user = Users.query.get(id)

    if not user:
        return jsonify({"message": "users doesn't exists", "data": {}}), 404
    
    try:
        db.session.delete(user)
        db.session.commit()
        result = user_schema.dump(user)
        return jsonify({"message": "user succesfully deleted", "data": result}), 200
    except:
        return jsonify({"message": "unable to delete", "data": {}}), 500
    
def user_by_username(username):
    try:
        return Users.query.filter(Users.username == username).one()
    except:
        return None
