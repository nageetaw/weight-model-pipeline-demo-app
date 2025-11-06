# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

app = FastAPI()

# allow your frontend/or Node backend origin
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # in prod set to your frontend origin
    allow_methods=["*"],
    allow_headers=["*"],
)


MODEL_PATH = os.environ.get("MODEL_PATH", "model.joblib")
model = None


def get_model():
    global model
    if model is None:
        from joblib import load
        model = load(MODEL_PATH)
    return model

class InputData(BaseModel):
    height: float

@app.get("/")
def welcome():
    return {"success":"Welcome your fastAPI server is working"}


@app.post("/predict")
def predict(data: InputData):
    m = get_model()
    h = [[data.height]]
    pred = m.predict(h)
    return {"height": data.height, "predicted_weight": float(pred[0])}

