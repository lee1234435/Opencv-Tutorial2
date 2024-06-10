import cv2
import numpy as np

image = cv2.imread("ex3\RGB.jpg")

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


blurred = cv2.GaussianBlur(gray, (5,5), 0)

edges = cv2. Canny(blurred,50,150)

contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


cv2.drawContours(image, contours, -1, (0,0,0),2)

cv2.imshow('Contours', image)

cv2.waitKey(0)
cv2.destroyAllWindows()