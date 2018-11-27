# app/auth/views.py


from flask import Flask, request, jsonify

from . import auth
from ..models import User

@auth.route('/')
def index():
    return 'Index Page'


@auth.route('/authentication/', methods=['GET'])
def authentication():
    if request.method == 'GET':
        email = request.args.get('email', None)
        password = request.args.get('password', None)
        if not all((email, password)):
            return jsonify({'error': {'description': "email and password are required"}}), 400
        exist = User.query.filter_by(email=email, password_hash=password).count()
        if exist:
            return jsonify({'data': 'login succesfull'}), 200
        else:
            return jsonify({'error':{'description': 'not found'}}), 404

