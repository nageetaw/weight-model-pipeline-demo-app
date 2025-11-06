# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import os


MODEL_PATH = os.environ.get("MODEL_PATH", "model.joblib")
model = load(MODEL_PATH)

app = FastAPI()

# allow your frontend/or Node backend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in prod set to your frontend origin
    allow_methods=["*"],
    allow_headers=["*"],
)

class InputData(BaseModel):
    height: float

@app.post("/predict")
def predict(data: InputData):
    h = [[data.height]]
    pred = model.predict(h)
    return {"height": data.height, "predicted_weight": float(pred[0])}
