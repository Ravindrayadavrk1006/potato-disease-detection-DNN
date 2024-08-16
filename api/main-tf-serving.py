from fastapi import FastAPI, UploadFile, File
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from core.logics import read_file_as_image
import tensorflow as tf
import numpy as np
import requests

app = FastAPI()
origins = [
    "http://localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins = origins,
    allow_credentials = True,
    allow_methods = ["*"],
    allow_headers = ["*"]
)
@app.get('/ping')
async def ping():
    return "hello, I am alive"

# model_location = 'D:/Repos/ml-ai/deep-neural-networks/deep-neural-network-project/models/1'

# MODEL = tf.keras.models.load_model(model_location)
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']


#if version is not specified then it will make call to the latest model
url = 'http://localhost:8501/v1/models/potato_disease:predict'

@app.post('/predict')
async def predict(
    file: UploadFile = File(...)
):
    np_image = read_file_as_image(await file.read())
    #here we are converting a 2d image into a batch since our model require batch input
    batched_image = np.expand_dims(
        np_image,
        axis=0)
    
    #json data for tf serving
    json_data = {
        "instances": batched_image.tolist()
    }
    try:
        response = requests.post(
            url=url,
            json=json_data
            )
        response.raise_for_status()
        #all images output hence it will be a 2d array
        all_predictions = response.json()["predictions"]
        #since out input contain single input hence getting that
        predictions = all_predictions[0]
        class_name = CLASS_NAMES[np.argmax(predictions)]
        confidence = np.round(100*(np.max(predictions)),2)
        #returning the class of predicted image
        return {
            "class": class_name,
            "confidence": confidence
        }
    except Exception as e:
        print(e)
        return "internal server error"

    
    



if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host = 'localhost',
        port=8000
        )

