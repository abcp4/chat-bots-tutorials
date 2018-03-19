from flask import Flask  
from flask import json  
from flask import Response  
from flask import request

inet_addr = "127.0.0.1"  
app = Flask(__name__)
token_client = "1769e13f5e037cde705ceb1230e5b6ed"
# *****************************************************************************************
# Create POST http://127.0.0.1:5000/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['POST'])
def postMethod():  
    value = request.form['name']
    print "form_value: " + value
    return json.dumps({"status": 200, "comment": "[ POST Method ] Hello " + value})

# *****************************************************************************************
# Read GET http://127.0.0.1:5000/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['GET'])
def getMethod(): 
    print("GET Console") 
    print("Token: ",request.args["hub.verify_token"])
    print("Challenge: ",request.args['hub.challenge'])
    return json.dumps({"status": 200, "comment": "[ Get Method ] Hello World data :"+str(request.data)})

# *****************************************************************************************
# Update PUT http://127.0.0.1:5000/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['PUT'])
def putMethod():  
    return json.dumps({"status": 200, "comment": "[ PUT Method ] Hello World"})

# *****************************************************************************************
# Delete DELETE http://127.0.0.1:5000/api/v1.0/print
# *****************************************************************************************
@app.route("/api/v1.0/print", methods=['DELETE'])
def deleteMethod():  
    return json.dumps({"status": 200, "comment": "[ DELETE Method ] Hello World"})

if __name__ == '__main__':  
    #app.debug = True
    print "inet_addr: " + inet_addr
    app.run(
        host = inet_addr,
        port = 5000
    )
