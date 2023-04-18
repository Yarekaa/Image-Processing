import numpy as np
import cv2
from cv2 import imread

# load image
img = imread('image/Parrots.jpg')

# padding
pad = cv2.copyMakeBorder(img, 50, 50, 50, 50, cv2.BORDER_CONSTANT, value=[0, 0, 0])

# display image
cv2.imshow('Padding', pad)
cv2.waitKey(0)
cv2.destroyAllWindows()