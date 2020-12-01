# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:17:50 2020

@author: dell
"""


import uvicorn
from fastapi import FastAPI
import pickle
from Diabetes import Diabetes
from sklearn.preprocessing import StandardScaler

app=FastAPI()

pickle_in = open("classifier_diabetic.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def Index():
    return "Welcome ALL"

@app.post('/predict')
def Predict(data:Diabetes):
    data=data.dict()
    
    Pregnancies=data['Pregnancies']
    Glucose=data['Glucose']
    Insulin=data['Insulin']
    BMI=data['BMI']
    DiabetesPF=data['DiabetesPF']
    Age=data['Age']
    prediction=classifier.predict([[Pregnancies,Glucose,Insulin,BMI,DiabetesPF,Age]])
    
    if(prediction[0]>0.5):
        prediction="you are likely to diabetic"
    else:
        prediction="No worries you are safe"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)