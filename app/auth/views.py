# app/auth/views.py


from flask import Flask, request, jsonify

from . import auth
from ..models import User

@auth.route('/')
def index():
    return 'Thank you for having us as your prefered authentication microservice, bye bye.'


@auth.route('/authentication/', methods=['GET'])
def authentication():
    if request.method == 'GET':
        email = request.args.get('email', None)
        password = request.args.get('password', None)
        if not all((email, password)):
            return jsonify({'error': {'description': "email and password are required"}}), 400
        user = User.query.filter_by(email=email).first()
        if user:
            if user.verify_password(password):
                return jsonify({'data': 
                            {'description': 'login successful',
                            'email': user.email,
                            'full_name': user.__str__()
                            }}), 200
            else:
                return jsonify({'error':{'description': 'wrong credentials'}}), 404
        else:
            return jsonify({'error':{'description': 'User not found'}}), 404

