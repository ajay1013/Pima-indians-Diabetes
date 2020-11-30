# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 00:28:50 2020

@author: dell
"""


from pydantic import BaseModel

class HeartDisease(BaseModel):
    age: int
    sex: str
    chest_pain: str
    resting_blood_pressure: int
    cholestoral: int
    fasting_blood_sugar: str
    resting_electrocardiographic_results: str
    maximum_heart_rate: int
    exercise_induced_angina: str
    ST_depression_induced_by_exercise_relative_to_rest: float
    slope_of_the_peak_exercise_ST_segment: int
    major_vessels_colored_by_flourosopy: str
    Thalassemia: str