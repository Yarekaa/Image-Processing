import numpy as np
import cv2
from cv2 import imread

# load image
img = imread('image/Parrots.jpg')

# resize 30x30
img = cv2.resize(img, (30, 30))

# resize 90x90
img2 = cv2.resize(img, (90, 90))

# resize 120x120
img3 = cv2.resize(img, (120, 120))

# display image
cv2.imshow('Resize', img)
cv2.imshow('90x90', img2)
cv2.imshow('120x120', img3)
cv2.waitKey(0)
cv2.destroyAllWindows()