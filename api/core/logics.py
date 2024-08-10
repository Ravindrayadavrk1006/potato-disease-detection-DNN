import numpy as np
from io import BytesIO
#pillow is used for reading data
from PIL import Image
# import tensorflow as tf

#for reading the image in np.array or ndarray format from bytes
def read_file_as_image(data)-> np.ndarray:
    bytes = BytesIO(data)
    pillow_img_object = Image.open(bytes)
    np_array  = np.array(pillow_img_object)
    return np_array