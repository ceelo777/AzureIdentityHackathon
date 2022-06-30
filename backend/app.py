from flask import Flask, render_template, request
import os
import configparser
from graph import Graph
from main import greet_user
# import tensorflow as tf 
# from tensorflow import keras 
# from keras.models import load_model

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

@app.route("/parseInbox", methods=["POST"])
@cross_origin()
def flaggedEmails(): 
    #receives array of emails, returns three dictionary/arrays of all emails marked red or green, and flagged vs. unflagged
    model = load_model("mymodel.h5")
    model._make_predict_function()
    good_emails = []
    bad_emails = []

    if request.method == 'POST': 
        myEmails = request.json['text']

        for email in myEmails: 
            preds = model.predict(email)
            if preds[0][0] > 0.5: 
                bad_emails.append(email)
            else: 
                good_emails.append(email)
    mydict = {}
    for email in myEmails: 
        if email in good_emails: 
            mydict[email] = 'green'
        else: 
            mydict[email] = 'red'
    
    return (mydict, good_emails, bad_emails)

@app.route("/showInbox", methods=["POST"])
@cross_origin()
def showEmails(): 
    config = configparser.ConfigParser()
    config.read(['config.cfg', 'config.dev.cfg'])
    azure_settings = config['azure']

    graph: Graph = Graph(azure_settings)

    greet_user(graph)

    return graph.get_inbox()

if __name__ == "__main__":
    showEmails()
    app.run()
