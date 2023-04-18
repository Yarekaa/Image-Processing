import numpy as np
import cv2
from cv2 import imread

# load image
img = imread('image/Parrots.jpg')

# rotate image
rows, cols, ch = img.shape
M = cv2.getRotationMatrix2D((cols/2, rows/2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

# display image
cv2.imshow('Rotation', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()