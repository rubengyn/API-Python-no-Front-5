from flask import Flask, jsonify,request
from threading import Thread
from flask_restful import Resource, Api
from flask_cors import CORS
import json
import random
import os

app = Flask('')
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

@app.route('/')
def home():
  return "estou online"


#################
##APi using Flask
###################

'''
@app.route('/api/input/<string:input_code>', methods=['GET,POST'])
def write_input(input_code):
  if request.method == 'GET':
    f = open("in", "w")
    f.write(input_code)
    f.close()
    return 'input gravado'
  elif request.method == 'POST':
    print('aki post')
    print( request.json['email'])
    return '2'

@app.route('/api/code/<string:code>', methods=['GET'])
def write_code(code):
  f = open("code.py", "w")
  f.write(code)
  f.close()
  return 'codigo gravado'

@app.route('/api/output/', methods=['get'])
def output():
  os.system("python code.py < in > out")
  out =''
  with open('out', 'r') as myfile:
    out = myfile.read()
  return out

@app.route('/api/output2/<string:output>', methods=['get'])
def output2(name):
  out =''
  with open('out', 'r') as myfile:
    out = myfile.read()
  return out

'''
@app.route('/api/input_post/', methods=['post'])
def write_input_post():
  json = request.get_json(force=True)  
  input_code = json['input']
  code = json['code']
  
  #gravar input
  f = open("in", "w")
  f.write(input_code)
  f.close()

  #gravar code
  f = open("code.py", "w")
  f.write(code)
  f.close()
  out =''
  try:  
    os.system("python code.py < in > out")
    with open('out', 'r') as myfile:
      out = myfile.read()
  except NameError:
    print(NameError)
    out = 'Erro\n\n'+NameError
    

  return out
  
def run():
  app.run(host='0.0.0.0',port=7210)
  
t = Thread(target=run)
t.start()