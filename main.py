from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import numpy as np
import pandas as pd

app = FastAPI()

# === CORS (development) ===
origins = [
    "http://127.0.0.1:5500",   # VSCode Live Server default
    "http://localhost:5500",
    "http://127.0.0.1:3000",   # optional if you use other ports
    "http://localhost:3000",
    # add more origins if you host frontend elsewhere
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,     # or ["*"] untuk semua origin saat development
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# === Load model & features ===
model = joblib.load("model_kolektibilitas.pkl")
feature_cols = joblib.load("feature_columns.pkl")

class InputData(BaseModel):
    data: dict

@app.get("/")
def home():
    return {"message": "API is running"}

@app.post("/predict")
def predict(input_data: InputData):
    # build DataFrame in correct column order (safer)
    df = pd.DataFrame([input_data.data])
    df = df.reindex(columns=feature_cols, fill_value=0)
    pred_shifted = model.predict(df)[0]
    pred_original = int(pred_shifted + 1)
    return {"prediction": pred_original}
