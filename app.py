# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:17:50 2020

@author: dell
"""


import uvicorn
from fastapi import FastAPI
import pickle
from HeartDisease import HeartDisease


app=FastAPI()

pickle_in = open("classifier_heart.pkl","rb")
classifier=pickle.load(pickle_in)

@app.get('/')
def Index():
    return "Welcome ALL"

@app.post('/predict')
def Predict(data:HeartDisease):
    data=data.dict()
    
    age=data['age']
    sex=data['sex']
    chest_pain=data['chest_pain']
    resting_blood_pressure=data['resting_blood_pressure']
    cholestoral=data['cholestoral']
    fasting_blood_sugar=data['fasting_blood_sugar']
    resting_electrocardiographic_results=data['resting_electrocardiographic_results']
    maximum_heart_rate=data['maximum_heart_rate']
    exercise_induced_angina=data['exercise_induced_angina']
    ST_depression_induced_by_exercise_relative_to_rest=data['ST_depression_induced_by_exercise_relative_to_rest']
    slope_of_the_peak_exercise_ST_segment=data['slope_of_the_peak_exercise_ST_segment']
    major_vessels_colored_by_flourosopy=data['major_vessels_colored_by_flourosopy']
    Thalassemia=data['Thalassemia']
    
    prediction=classifier.predict([[age,sex,chest_pain,resting_blood_pressure,cholestoral,fasting_blood_sugar,resting_electrocardiographic_results,maximum_heart_rate,exercise_induced_angina,ST_depression_induced_by_exercise_relative_to_rest,slope_of_the_peak_exercise_ST_segment,major_vessels_colored_by_flourosopy,Thalassemia]])
    
    if(prediction[0]>0.6):
        prediction="you are likely to have a heart disease"
    else:
        prediction="No worries you are safe"
    return {
        'prediction': prediction
    }

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=5000)