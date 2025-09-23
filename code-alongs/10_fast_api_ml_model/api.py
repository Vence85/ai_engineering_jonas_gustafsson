from fastapi import FastAPI, APIRouter
import pandas as pd
import joblib
from constants import DATA_PATH, MODELS_PATH
from pydantic import BaseModel, Field

df = pd.read_csv(DATA_PATH / "Iris.csv")

router = APIRouter(prefix = "/api/iris/v1")

app = FastAPI()



class IrisInput(BaseModel):
    sepal_length: float = Field(gt = 4, lt = 8.5)
    sepal_width: float = Field(gt = 1.8, lt = 5)
    petal_length: float = Field(gt = 0.8, lt = 7.5)
    petal_width: float = Field(gt = 0, lt = 3)

class PredicitonOutpt(BaseModel):
    predicted_flower:str


@router.get("/api/iris/v1")
def read_data():
    return df.to_dict(orient="records")

@router.post("/predict", response_model=PredicitonOutpt)
def predict_flower(payload: IrisInput):
    data_to_predict = pd.DataFrame(payload.model_dump(), index = [0])
    clf = joblib.load(MODELS_PATH / "iris_classifier.joblib")
    prediction = clf.predict(data_to_predict)
    return {"predicted_flower": prediction}



app.include_router(router=router)

