#!/usr/bin/python3

from flask import Flask, request, abort
from common import error_handler

app = Flask(__name__)
error_handler.register_errors(app)

users = {
    '1': {'userId': '1', 'username': 'csp1'},
    '2': {'userId': '2', 'username': 'csp2'}
}


def run_server():
    app.run()


def check_existence(user_id):
    if user_id not in users:
        abort(404)


@app.route('/')
def welcome():
    return 'Welcome!'


@app.route('/users', methods=['GET'])
def list_users():
    return users


@app.route('/users/<user_id>', methods=['GET'])
def get_user(user_id):
    device_id = request.args.get('deviceId')
    print('deviceId = ', device_id)
    check_existence(user_id)
    return users[user_id]


@app.route('/users/<user_id>', methods=['POST'])
def create_user(user_id):
    data = request.json
    users[user_id] = data
    return users[user_id]


@app.route('/users/<user_id>', methods=['DELETE'])
def delete_user(user_id):
    check_existence(user_id)
    del users[user_id]
    return 'ok'
