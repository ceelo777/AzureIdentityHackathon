# import tensorflow_text
import numpy as np
from flask import Flask, render_template, request
import os
import configparser
from graph import Graph
from main import greet_user
import json
import random
import re
# import tensorflow as tf 
# from tensorflow import keras 
# from keras.models import load_model
# import tensorflow_hub as hub

os.environ['KMP_DUPLICATE_LIB_OK']='True'
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/submitText", methods=["POST"])
@cross_origin()
def receive():

    # model = load_model("mymodel.h5", custom_objects={'KerasLayer':hub.KerasLayer})
    # model.make_predict_function()
    myEmail = request.json['text']
    # preds = model.predict(myEmail)
    
    # if preds[0][0] > 0.5:
    # isSpam = True
    # else:
    # isSpam = False
    
    isSpam = False
    isPasswordDict = {}
    
    words = myEmail.split(' ')
    isPasswordDict["spam"] = isSpam
    for word in words:
        if re.match(r"^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{6,16}$", word):
            isPasswordDict[word] = True
        else:
            isPasswordDict[word] = False
            
    print(isPasswordDict)
    json_string = json.dumps(isPasswordDict)
    print(json_string)
    with open('../frontend/src/password_json_data.json', 'w') as outfile:
        outfile.write(json_string)    

#    if request.method == 'POST':
#        print(request.json['text'])

    return isPasswordDict

@app.route("/parseInbox", methods=["GET"])
@cross_origin()
def flaggedEmails(): 
    #receives array of emails, returns three dictionary/arrays of all emails marked red or green, and flagged vs. unflagged
    # model = load_model("mymodel.h5", custom_objects={'KerasLayer':hub.KerasLayer})
    # model.make_predict_function()
    good_emails = []
    bad_emails = []
    
    if request.method == 'GET': 
        #myEmails = request.json['text']
        myEmails = []
        data = None
        with open('json_data.json') as f:
            data = json.load(f)
            for val in data['value']:
                myEmails.append(val['subject'])
        for email in myEmails: 
            email = np.array([email])
            # preds = model.predict(email)
            if random.randint(0, 1) > 0.5: 
                bad_emails.append(email)
            else: 
                good_emails.append(email)
    mydict = {}

    # myEmails = []
    for email in myEmails: 
        if email in good_emails: 
            mydict[email] = 'green'
        else: 
            mydict[email] = 'red'
    
    print(mydict, good_emails, bad_emails)

    json_string = json.dumps(mydict)
    with open('../frontend/src/json_data_status.json', 'w') as outfile:
        outfile.write(json_string)
    return mydict

@app.route("/showInbox", methods=["GET"])
@cross_origin()
def showEmails(): 
    resp = graph.get_inbox()
    json_string = json.dumps(resp)
    print(json_string)
    with open('json_data.json', 'w') as outfile:
        outfile.write(json_string)
    return "complete"

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']
    graph: Graph = Graph(azure_settings)
    app.run()
