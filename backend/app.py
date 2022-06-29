from flask import Flask, render_template, request
import os
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

if __name__ == "__main__":
    app.run()