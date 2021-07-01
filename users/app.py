import json
import boto3
from flask_lambda import FlaskLambda
from flask import request, jsonify


app = FlaskLambda(__name__)
ddb = boto3.resource('dynamodb')
table = ddb.Table('users')


@app.route('/')
def index():
    return json_response({"message": "Hello, Users!"})


@app.route('/users', methods=['GET', 'POST'])
def list_create_users():
    """
        List user endpoints (GET request)
        Create user endpoints (Post request)
    """
    if request.method == 'GET':
        users = table.scan()['Items']
        return json_response(users)
    else:
        table.put_item(Item=request.form.to_dict())
        return json_response({"message": "users entry created"})



@app.route('/users/<id>', methods=['GET', 'PATCH', 'DELETE'])
def get_patch_delete_users(id):
    """
        List user by id (Get request)
        Update user by id (patch request)
        Delete user bt id (delete request)
    """
    key = {'id': id}
    if request.method == 'GET':
        user = table.get_item(Key=key).get('Item')
        if user:
            return json_response(user)
        else:
            return json_response({"message": "user not found"}, 404)
    elif request.method == 'PATCH':
        attribute_updates = {key: {'Value': value, 'Action': 'PUT'}
                             for key, value in request.form.items()}
        table.update_item(Key=key, AttributeUpdates=attribute_updates)
        return json_response({"message": "users entry updated"})
    else:
        table.delete_item(Key=key)
        return json_response({"message": "users entry deleted"})



@app.errorhandler(404)
def resource_not_found(e):
    """
        Page not found 
    """
    return json_response({"message": "Page, not found"}, 404)


def json_response(data, response_code=200):
    return json.dumps(data), response_code, {'Content-Type': 'application/json'}