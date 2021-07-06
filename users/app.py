from flask import Flask, request, jsonify, Response
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.exc import IntegrityError
import os
import json

# Init app
app = Flask(__name__)

# basedir
basedir = os.path.abspath(os.path.dirname(__file__))

# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + \
    os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init db
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)

    def __init__(self, email, first_name, last_name, password):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    def json(self):
        return {'id': self.id, 'email': self.email, 'first_name':  self.first_name, 'last_name': self.last_name,
                'password': self.password}


# Home
@app.route("/")
def index():
    return "Icompass REST API"


# GET /user
@app.route('/user', methods=['GET'])
def get_all_users():
    users = User.query.all()
    output = [User.json(user) for user in users]
    response = jsonify({'message': output})
    response = jsonify({'users': output})
    response.status_code = 200
    return response


# GET /user/<id>
@app.route('/user/<id>', methods=['GET'])
def get_one_user(id):
    try:
        user = User.query.filter_by(id=id).first_or_404()
        user_data = {}
        user_data['id'] = user.id
        user_data['email'] = user.email
        user_data['first_name'] = user.first_name
        user_data['last_name'] = user.last_name
        user_data['password'] = user.password
        response = jsonify({'user': user_data})
        response.status_code = 200
        return response
    except:
        return not_found("User not found!")


# POST /user
@app.route('/user', methods=['POST'])
def create_user():
    request_data = request.get_json()
    if (validPostRequestData(request_data)):
        try:
            email = request.json['email']
            first_name = request.json['first_name']
            last_name = request.json['last_name']
            hash_password = generate_password_hash(
                request.json['password'], method='sha256')

            new_user = User(email, first_name, last_name, hash_password)
            db.session.add(new_user)
            db.session.commit()
            response = jsonify({'message': 'The User is created'})
            response.status_code = 201
            return response
        except IntegrityError:
            db.session.rollback()
            return "This email id already exists"
    else:
        invalidPostRequestDataErrorMsg = {
            "error": "Invalid book object passed in request",
            "helpString": "Data passed in similar to this {'email': 'email@gmail.com', 'first_name': 'firstname','last_name': 'last_name', 'passsword': 'password' }"
        }
        response = jsonify(invalidPostRequestDataErrorMsg)
        response.status_code = 400
        response.mimetype = 'application/json'
        return response


# PATCH /user/<id>
@app.route('/user/<id>', methods=['PATCH'])
def update_product(id):

    try:
        request_data = request.get_json()
        user_update = User.query.filter_by(id=id).first()
        if("email" in request_data):
            user_update.email = request_data['email']
        elif("first_name" in request_data):
            user_update.first_name = request_data['first_name']
        elif("last_name" in request_data):
            user_update.last_name = request_data['last_name']
        elif("password" in request_data):
            user_update.password = generate_password_hash(
                request_data['password'], method='sha256')
        else:
            return bad_request("Invalid data")
        db.session.commit()
        response = jsonify({'message': 'User Update Successfully!'})
        response.status_code = 200
        return response
    except:
        return bad_request("Invalid data")


# DELETE /user/<id>
@app.route('/user/<id>', methods=['DELETE'])
def delete_user(id):
    try:
        user = User.query.filter_by(id=id).first()
        db.session.delete(user)
        db.session.commit()
        response = jsonify({'message': 'The user has been deleted!'})
        response.status_code = 200
        return response
    except:
        return not_found("User not found!")


# Invalid URL
@app.errorhandler(404)
def resource_not_found(e):
    response = jsonify({"message": "Page, not found"})
    response.status_code = 404
    return response


# Not found
def not_found(message):
    response = jsonify({'error': message})
    response.status_code = 404
    return response


# Invalid request
def bad_request(message):
    response = jsonify({'error': message})
    response.status_code = 400
    return response


# Validate Post request
def validPostRequestData(User):
    if ("email" in User and "first_name" in User and "last_name" in User and "password" in User):
        return True
    else:
        return False


if __name__ == '__main__':
    app.run(debug=True)
