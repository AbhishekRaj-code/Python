import cv2

img = cv2.imread("resized_waterfall.jpg")

print("Dimention of the image :", img.shape)

width = 720
height =880
dim = (width, height)
resized = cv2.resize(img, dim)

cv2.imshow("window", resized)

cv2.waitKey(0)

cv2.destroyAllWindows()