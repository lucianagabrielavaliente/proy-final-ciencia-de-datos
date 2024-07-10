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


model = joblib.load("Model.pkl")

app = FastAPI()

@app.post("/predict/")
def predit(data: InputData):
    input_values = np.array([data.bloodPressureMax, data.bloodPressureMin, data.gender, data.age, data.occupation, data.sleepDuration, data.qualityOfSleep, data.physicalActivityLevel, data.stressLevel, data.bmi, data.heartRate, data.dailySteps], dtype=float).reshape(1, -1)
    scaler = StandardScaler()
    scaled_input = scaler.fit_transform(input_values)
    prediction = model.predict(scaled_input)[0]
    prediction_result = float(prediction)
    return {"Prediction": prediction_result}
