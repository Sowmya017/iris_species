import uvicorn 
from fastapi import FastAPI 
from iris_model import IrisModel
import pandas as pd
import numpy as np 
import pickle 

app = FastAPI()

pickle_in =open('Rf.pkl', 'rb')
classifer = pickle.load(pickle_in)
@app.get('/')
async def index():
    return {'msg':'hello, world'}

@app.post('/predict')
def predict_species(data:IrisModel):
    data = data.dict()
    sepal_length = data['sepal_length']
    sepal_width  = data['sepal_width'] 
    petal_length = data ['petal_length']
    petal_width  = data['petal_width']

    predict = classifer.predict([[sepal_length,sepal_width,petal_length,petal_width]])
     # Map numeric prediction to class label
    label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    predicted_label = label_map[predict[0]]
    
    return {
        "prediction": int(predict[0]),
        "species": predicted_label
    }