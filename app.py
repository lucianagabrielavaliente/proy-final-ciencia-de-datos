from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from sklearn.preprocessing import StandardScaler
import numpy as np

class InputData(BaseModel):
    bloodPressureMax: float
    bloodPressureMin: float
    gender: float
    age: float
    occupation: float
    sleepDuration: float
    qualityOfSleep: float
    physicalActivityLevel: float
    stressLevel: float
    bmi: float
    heartRate: float
    dailySteps: float


model = joblib.load("LR-Model.pkl")

app = FastAPI()

@app.post("/predict/")
def predit(data: InputData):
    input_values = np.array([data.bloodPressureMax, data.bloodPressureMin, data.gender, data.age, data.occupation, data.sleepDuration, data.qualityOfSleep, data.physicalActivityLevel, data.stressLevel, data.bmi, data.heartRate, data.dailySteps], dtype=float).reshape(1, -1)
    scaler = StandardScaler()
    scaled_input = scaler.fit_transform(input_values)
    prediction = model.predict(scaled_input)[0]
    prediction_result = float(prediction)
    if prediction_result == 0:
        return{"You don't have any sleep disorder"}
    elif prediction_result == 1:
        return{"You may be suffering from a sleep disorder, please talk to your primary care physician."}
    else:
        return{"There has been an error in the prediction."}
