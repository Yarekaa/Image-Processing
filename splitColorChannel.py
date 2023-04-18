import numpy as np
import cv2
from cv2 import imread

# load image
img = imread('image/Parrots.jpg')

# split the image into color channels
(b, g, r) = cv2.split(img)

# merge the image back together
merged = cv2.merge([b, g, r])

# concatenate the images along the x-axis (i.e., from left to right)
concatenated = np.concatenate([b, g, r], axis=1)

# display image
cv2.imshow('Blue', concatenated)
cv2.imshow('Merged', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()