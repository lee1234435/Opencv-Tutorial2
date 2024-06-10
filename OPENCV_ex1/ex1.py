import cv2
import numpy as np



image = cv2.imread("ex1\RGB.jpg")

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)

lower_white = np.array([0,0,255], dtype=np.uint8)
upper_white = np.array([255,30,255], dtype=np.uint8)
white_mask = cv2.inRange(hsv,lower_white,upper_white)
white_result = cv2.bitwise_and(image,image,mask=white_mask)

cv2.imshow("original", image)
cv2.imshow("white", white_result)

cv2.waitKey(0)
cv2.destroyAllWindows()

