import requests 
import numpy as np
import tensorflow as tf
image_sample = np.random.rand(256, 256, 3)

# Convert to an array of unsigned integers (0-255) to represent pixel values
image_sample = (image_sample * 255).astype(np.uint8)

image_within_batch = tf.expand_dims(image_sample, axis=0)

url = "http://localhost:8501/v1/models/potato_disease:predict"
data = {
	"instances": [image_within_batch]
}

predictions = requests.post(url=url,data=data, verify=False)
print(predictions) 