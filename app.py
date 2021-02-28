import numpy as np
import pandas as pd
from flask import Flask, request, jsonify, render_template, url_for, redirect
import pickle
from pycaret.classification import *

app = Flask(__name__)
model = load_model('final_stroke_model')
cols = ['gender', 'age', 'hypertension', 'heart_disease', 'ever_married', 'work_type', 'Residence_type', 'avg_glucose_level', 'bmi']

@app.route('/')
def home():
    return render_template('index.html') 

@app.route('/predict',methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    features = [x for x in request.form.values()]
    print(features)
    features_df = pd.DataFrame([], columns = cols)
    features_df.loc[0] = features
    prediction = predict_model(model, data = features_df)
    output = int(prediction.Label[0])
    if output==0:
        output = 'low'
    else:
        output ='high'

    return render_template('index.html', prediction_text='The chances are {}!'.format(output))



if __name__ == "__main__":
    app.run(debug=True)