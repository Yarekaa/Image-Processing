import numpy as np
import cv2
from cv2 import imread

# load the image
img = imread('image/Parrots.jpg')

# to crop
y, x, h, w = 0, 0, 400, 400
crop = img[y:y+h, x:x+w]

# display image
cv2.imshow('Cropping', crop)
cv2.waitKey(0)
cv2.destroyAllWindows()