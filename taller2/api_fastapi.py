from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.externals import joblib

app = FastAPI()

class InferenceRequest(BaseModel):
    # Define la estructura de los datos de entrada para la inferencia
    feature1: float
    feature2: float
    feature3: float

class InferenceResponse(BaseModel):
    prediction: float

class InferencePipeline:
    def __init__(self):
        # Cargar el modelo previamente entrenado al iniciar la aplicación
        self.model = joblib.load("your_model.pkl")

    def perform_inference(self, data: InferenceRequest) -> float:
        # Lógica para realizar la inferencia con el modelo cargado
        # data es la entrada para la inferencia
        input_data = [[data.feature1, data.feature2, data.feature3]]
        result = self.model.predict(input_data)
        return float(result[0])

inference_pipeline = InferencePipeline()

@app.post("/predict", response_model=InferenceResponse)
def predict(data: InferenceRequest):
    try:
        # Realizar inferencia usando el modelo cargado
        result = inference_pipeline.perform_inference(data)

        # Devolver el resultado como respuesta JSON
        return {"prediction": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sklearn.externals import joblib

app = FastAPI()

class InferenceRequest(BaseModel):
    # Define la estructura de los datos de entrada para la inferencia
    feature1: float
    feature2: float
    feature3: float

class InferenceResponse(BaseModel):
    prediction: float

class InferencePipeline:
    def __init__(self):
        # Cargar el modelo previamente entrenado al iniciar la aplicación
        self.model = joblib.load("your_model.pkl")

    def perform_inference(self, data: InferenceRequest) -> float:
        # Lógica para realizar la inferencia con el modelo cargado
        # data es la entrada para la inferencia
        input_data = [[data.feature1, data.feature2, data.feature3]]
        result = self.model.predict(input_data)
        return float(result[0])

inference_pipeline = InferencePipeline()

@app.post("/predict", response_model=InferenceResponse)
def predict(data: InferenceRequest):
    try:
        # Realizar inferencia usando el modelo cargado
        result = inference_pipeline.perform_inference(data)

        # Devolver el resultado como respuesta JSON
        return {"prediction": result}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
