import numpy as np

import io
import json
import cv2
import os


def read_cv2_images(img):
    readStream = io.BytesIO(img)
    image =  np.asarray(bytearray(readStream.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
    return image
