from flask import Flask, request
from operations import *

app = Flask(__name__)

@app.route('/add')
def add_route():
  a = request.args["a"]
  b = request.args["b"]
  result = str(add(int(a), int(b)))
  return result

@app.route('/sub')
def sub_route():
  a = request.args["a"]
  b = request.args["b"]
  result = str(sub(int(a), int(b)))
  return result

@app.route('/mult')
def mult_route():
  a = request.args["a"]
  b = request.args["b"]
  result = str(mult(int(a), int(b)))
  return result


@app.route('/div')
def div_route():
  a = request.args["a"]
  b = request.args["b"]
  result = str(div(int(a), int(b)))
  return result
