# main.py
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import os

# --- FastAPI instance ---
app = FastAPI(title="Height → Weight Predictor API")

# --- CORS setup ---
# Replace "*" with your frontend URL in production for security
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # e.g., ["https://weight-model-pipeline-demo-app.vercel.app"]
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- ML Model Setup ---
MODEL_PATH = os.environ.get("MODEL_PATH", "model.joblib")
model = None  # Lazy load model to avoid slow startup

def get_model():
    global model
    if model is None:
        from joblib import load
        model = load(MODEL_PATH)
    return model

# --- Pydantic input model ---
class InputData(BaseModel):
    height: float

# --- Routes ---
@app.get("/")
def welcome():
    return {"success": "Welcome! FastAPI server is running."}

@app.post("/api/predict")
def predict(data: InputData):
    m = get_model()
    h = [[data.height]]
    pred = m.predict(h)
    return {"height": data.height, "predicted_weight": float(pred[0])}

# --- Entry point for local testing only ---
if __name__ == "__main__":
    import uvicorn
    port = int(os.environ.get("PORT", 8000))  # Default to 8000 if not set
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
