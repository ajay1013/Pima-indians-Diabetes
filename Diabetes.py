# -*- coding: utf-8 -*-
"""
Created on Wed Dec  2 01:22:06 2020

@author: dell
"""


from pydantic import BaseModel

class Diabetes(BaseModel):
    Pregnancies: int
    Glucose: int
    Insulin: int
    BMI: int
    DiabetesPF: int
    Age: int