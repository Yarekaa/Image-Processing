import numpy as np
import cv2
from cv2 import imread

# load image
img = imread('image/Parrots.jpg')

# perspective transform
pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv2.getPerspectiveTransform(pts1,pts2)
dst = cv2.warpPerspective(img,M,(500,500))

# display the image
cv2.imshow('Perspective Transform', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()