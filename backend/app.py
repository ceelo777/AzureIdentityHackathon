from flask import Flask, render_template, request
import os
import configparser
from graph import Graph
from main import greet_user
import tensorflow as tf 
from tensorflow import keras 
from keras.models import load_model
import tensorflow_hub as hub

os.environ['KMP_DUPLICATE_LIB_OK']='True'
from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/submitText", methods=["POST"])
@cross_origin()
def receive():
    # global model
    # model = load_model("mymodel.h5")
    # model._make_predict_function()

    if request.method == 'POST':         
        print(request.json['text'])

    return "Hello, World!"

@app.route("/parseInbox", methods=["GET"])
@cross_origin()
def flaggedEmails(): 
    #receives array of emails, returns three dictionary/arrays of all emails marked red or green, and flagged vs. unflagged
    model = load_model("mymodel.h5", custom_objects={'KerasLayer':hub.KerasLayer})
    model._make_predict_function()
    good_emails = []
    bad_emails = []

    
    if request.method == 'GET': 
        #myEmails = request.json['text']
        myEmails = ['hello my name is chris']
        for email in myEmails: 
            preds = model.predict(email)
            if preds[0][0] > 0.5: 
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
    return (mydict, good_emails, bad_emails)

@app.route("/showInbox", methods=["GET"])
@cross_origin()
def showEmails(): 
    resp = graph.get_inbox()
    print("Inbox: ", resp)
    return resp

if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']
    graph: Graph = Graph(azure_settings)
    app.run()
