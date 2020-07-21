# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 17:03:00 2020

@author: Ajay Kumar
"""


from flask import Flask, request
import pickle
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

pickle_in=open("classifier_diabetic.pkl", "rb")
classifier=pickle.load(pickle_in)

@app.route("/")
def welcome():
    return  "welcome everyone"

    
@app.route("/predict", methods=["GET"])
def Diabetic_prediction():
    
    """Let's Authenticate whether a person is diabetic or not
    This is using docstrings for specifications.
    ---
    parameters:  
      - name: Pregnancies
        in: query
        type: number
        required: true
        
      - name: Glucose
        in: query
        type: number
        required: true
        
      - name: Insulin
        in: query
        type: number
        required: true
        
      - name: BMI
        in: query
        type: number
        required: true
        
      - name: DiabetesPF
        in: query
        type: number
        required: true
        
      - name: Age
        in: query
        type: number
        required: true
        
    responses:
        200:
            description: The output values
        
    """
    
    Pregnancies=request.args.get("Pregnancies")
    Glucose=request.args.get("Glucose")
    Insulin=request.args.get("Insulin")
    BMI=request.args.get("BMI")
    DiabetesPF=request.args.get("DiabetesPF")
    Age=request.args.get("Age")
    
    Pregnancies=float(Pregnancies)
    Glucose=float(Glucose)
    Insulin=float(Insulin)
    BMI=float(BMI)
    DiabetesPF=float(DiabetesPF)
    Age=float(Age)
    
    Pregnancies = ((Pregnancies) - 3.845052)/3.369578
    Glucose=((Glucose) - 120.894531)/31.972618
    Insulin=((Insulin) - 79.799479)/115.244002
    BMI=((BMI) - 31.992578)/7.884160
    DiabetesPF=((DiabetesPF) - 0.471876)/0.331329
    Age=((Age) - 33.240885)/11.760232
    
    prediction=classifier.predict([[Pregnancies, Glucose, Insulin, BMI, DiabetesPF, Age]])
    print(prediction)
    return "Hello The answer is " + str(prediction)

if __name__=="__main__":
    app.run()