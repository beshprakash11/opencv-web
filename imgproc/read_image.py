import numpy as np

import io
import cv2

def pre_process(img):
    
    return img
def read_cv2_images(img):
    readStream = io.BytesIO(img)
    image =  np.asarray(bytearray(readStream.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
