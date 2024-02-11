from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
import os
from src.models.train import train


os.chdir(os.path.dirname(os.path.abspath(__file__)))


model_RF = joblib.load('../../models/random_forest_model.joblib')
model_GB = joblib.load('../../models/gradient_boosting_model.joblib')
label_encoder = joblib.load('../../models/label_encoder.joblib')
sex_encoder = joblib.load('../../models/sex_encoder.joblib')


class Penguin(BaseModel):
    studyName: str = "PAL0708"
    SampleNumber: int = 1
    Region: str = "Anvers"
    Island: str = "Torgersen"
    Stage: str = "Adult, 1 Egg Stage"
    IndividualID: str = "N1A1"
    ClutchCompletion: str = "Yes"
    DateEgg: str = "11/11/87"
    CulmenLength_mm: float = 39.1
    CulmenDepth_mm: float = 18.7
    FlipperLength_mm: float = 181.0
    BodyMass_g: float = 3750.0
    Sex: str = "MALE"
    Delta_15_N: float = 8.94
    Delta_13_C: float = -24.69
    Comments: str = "Not enough.."
    
app = FastAPI()

@app.get("/")
async def root():
    
    return {"message": "Hola mundo!"}

@app.post("/predict_RF/")
def predict_species_random_forest(penguin: Penguin):
    sex_encoded = sex_encoder.transform(np.array([penguin.Sex]).ravel())
    features = np.array([
        penguin.CulmenLength_mm,
        penguin.CulmenDepth_mm,
        penguin.FlipperLength_mm,
        penguin.BodyMass_g,
        sex_encoded.item(),
        penguin.Delta_15_N,
        penguin.Delta_13_C
    ]).reshape(1,-1)

    prediction = model_RF.predict(features)
    species = label_encoder.inverse_transform(prediction)[0]
    return{"Predicted species by Random Forest": species}

@app.post("/predict_GBM/")
def predict_species_GBM(penguin: Penguin):
    sex_encoded = sex_encoder.transform(np.array([penguin.Sex]).ravel())
    features = np.array([
        penguin.CulmenLength_mm,
        penguin.CulmenDepth_mm,
        penguin.FlipperLength_mm,
        penguin.BodyMass_g,
        sex_encoded.item(),
        penguin.Delta_15_N,
        penguin.Delta_13_C
    ]).reshape(1,-1)

    prediction = model_GB.predict(features)
    species = label_encoder.inverse_transform(prediction)[0]
    return{"Predicted species by GBM": species}

@app.post("/train/")
def train_models():
    train() 