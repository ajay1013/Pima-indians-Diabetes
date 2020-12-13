# -*- coding: utf-8 -*-
"""
Created on Fri Dec 11 16:37:12 2020

@author: dell
"""


import pickle
import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from flask import Flask, request, render_template



app = Flask(__name__)

model = pickle.load(open('classifier_diabetic.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('Diabetes.html')

@app.route('/predict',methods=['POST'])
def predict():
    int_features = [float(x) for x in request.form.values()]
    features = [np.array(int_features)]
    feat = pd.DataFrame(data=features, columns=["Pregnancies","Glucose","BloodPressure","SkinThickness","Insulin","BMI","DiabetesPF","Age"])
    final_features = pd.DataFrame(StandardScaler().fit_transform(feat))
    prediction = model.predict(final_features)
    if prediction==1:
        return render_template('Diabetes.html', prediction_text='Sorry but you are likely to be diabetic')
    else:
        return render_template('Diabetes.html', prediction_text='Great you are safe as per your test results')

if __name__ == "__main__":
    app.run(port=12000)
