from flask import Flask, render_template, request
import tensorflow as tf 
from tensorflow import keras 
from keras.models import load_model

app = Flask(__name__)


@app.route("/submitText")
def receive():
    # global model
    # model = load_model("mymodel.h5")
    # model._make_predict_function()

    if request.method == 'POST': 
        print(request.json['body'])

    
    return "Hello, World!"

if __name__ == "__main__":
    app.run()