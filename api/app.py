from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd
import os


class PredictionInput(BaseModel):
    Brand: int
    Processor_Speed: float
    RAM_Size: int
    Storage_Capacity: int
    Screen_Size: float
    Weight: float


def load_model():
    # Load model from project root alongside rf_model.pkl
    current_dir = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.abspath(os.path.join(current_dir, "..", "rf_model.pkl"))
    return joblib.load(model_path)


app = FastAPI(title="Laptop Price Predictor API")
model = load_model()


@app.get("/")
def root():
    return {"status": "ok", "message": "Laptop Price Predictor API"}


@app.post("/predict")
def predict(payload: PredictionInput):
    input_df = pd.DataFrame(
        {
            "Brand": [payload.Brand],
            "Processor_Speed": [payload.Processor_Speed],
            "RAM_Size": [payload.RAM_Size],
            "Storage_Capacity": [payload.Storage_Capacity],
            "Screen_Size": [payload.Screen_Size],
            "Weight": [payload.Weight],
        }
    )

    price = float(model.predict(input_df)[0])
    return {"price": price}


