import cv2
import numpy as np

img = cv2.imread("resized_waterfall.jpg")

width = 360
height = 400
dim = (width, height)

resized = cv2.resize(img, dim)

cv2.imshow("Original", resized)

flip1 = cv2.flip(resized, 1)
flip2 = cv2.flip(resized, 0)
flip3 = cv2.flip(resized, -1)

cv2.imshow("Horizontal", flip1)
cv2.imshow("Vertical", flip2)
cv2.imshow("Horizontal+Vertical", flip3)

cv2.waitKey(0)
cv2.destroyAllWindows()