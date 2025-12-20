import cv2
import numpy as np

img = cv2.imread("waterfall_m.jpg", cv2.IMREAD_COLOR)
img2 = np.zeros(shape= [400, 600, 3], dtype='uint8')

cv2.line(img, (0,0), (200,200), (310,0,0),3)

cv2.rectangle(img, (200,150), (300,350),(0,255,0), 3)

cv2.circle(img, (300,100), 80, (255,0,255),3)

pts_polygon = np.array([[100,80],[100,300],[500,80],[500,300]], np.int32)

cv2.polylines(img, [pts_polygon], True, (0,255,255),3)

font = cv2.FONT_HERSHEY_DUPLEX

cv2.putText(img, 'HELLO!', (10,500), font, 3, (200,255,255), 8, cv2.LINE_AA)



cv2.line(img2, (0,0), (200,200), (310,0,0),3)

cv2.rectangle(img2, (200,150), (300,350),(0,255,0), 3)

cv2.circle(img2, (300,100), 80, (255,0,255),3)

cv2.polylines(img2, [pts_polygon], True, (0,255,255),3)

cv2.putText(img2, 'HELLO!', (10,500), font, 3, (200,255,255), 8, cv2.LINE_AA)

cv2.imshow('Image', img)
cv2.imshow('Image', img2)

cv2.waitKey(0)
cv2.destroyAllWindows

