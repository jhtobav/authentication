from flask import Flask, request
app = Flask(__name__)


@app.route('/')
def index():
    return 'Index Page'


@app.route('/authentication/', methods=['GET'])
def authentication():
    email = request.args.get('email', None)
    password = request.args.get('password', None)
    return 'User : {}-{}'.format(email, password)
