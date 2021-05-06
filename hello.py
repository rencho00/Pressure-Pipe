from flask import Flask

hello = Flask(__name__)


@hello.route('/')

def index():

    return '<h1>Hesfsfds World </h1>'