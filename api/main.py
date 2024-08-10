from fastapi import FastAPI, UploadFile, File
import uvicorn
from core.logics import read_file_as_image
import tensorflow as tf
import numpy as np
app = FastAPI()

@app.get('/ping')
async def ping():
    return "hello, I am alive"

model_location = 'D:/Repos/ml-ai/deep-neural-networks/deep-neural-network-project/models/saved_model'

MODEL = tf.keras.models.load_model(model_location)
CLASS_NAMES = ['Potato___Early_blight', 'Potato___Late_blight', 'Potato___healthy']

@app.post('/predict')
async def predict(
    file: UploadFile = File(...)
):
    np_image = read_file_as_image(await file.read())
    #here we are converting a 2d image into a batch since our model require batch input
    batched_image = tf.expand_dims(
        np_image,
        axis=0)
    predictions = MODEL.predict(batched_image)
    class_name = CLASS_NAMES[np.argmax(predictions)]
    confidence = np.round(100*(np.max(predictions)),2)
    #returning the class of predicted image
    return {
        "class": class_name,
        "confidence": confidence
    }
    # return "image uploaded successfully"
    
    



if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host = 'localhost',
        port=8000
        )

