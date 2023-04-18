import numpy as np
import cv2
from cv2 import imread

# read the image
img = imread('image/Parrots.jpg')

# show the image
cv2.imshow('RGB', img)
cv2.waitKey(0)
cv2.destroyAllWindows()