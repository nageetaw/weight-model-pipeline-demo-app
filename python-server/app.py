# app.py
from fastapi import FastAPI
from pydantic import BaseModel
from joblib import load
from fastapi.middleware.cors import CORSMiddleware
import os
import uvicorn

port = int(os.environ.get("PORT", 8000)) 

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

@app.get("/")
def welcome():
    return {"success":"Welcome your fastAPI server is working"}

@app.post("/predict")
def predict(data: InputData):
    h = [[data.height]]
    pred = model.predict(h)
    return {"height": data.height, "predicted_weight": float(pred[0])}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)