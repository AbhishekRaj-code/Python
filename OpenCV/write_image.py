import cv2

img = cv2.imread("waterfall_m.jpg", 0)

cv2.imshow("window", img)

cv2.imwrite('waterfall.jpg', img)

cv2.waitKey(0)

cv2.destroyAllWindows()