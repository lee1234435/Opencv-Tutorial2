import cv2
import numpy as np

cap = cv2.VideoCapture(0)

# cap = cv2.VideoCapture("ex2/video.mp4")
# "ex2/video.mp4"

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    lower_white = np.array([0,0,200], dtype=np.uint8)
    upper_white = np.array([255,30,255], dtype=np.uint8)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)
    
    
    white_result = cv2.bitwise_and(frame, frame, mask=white_mask)
    
    cv2.imshow('original', frame)
    cv2.imshow('white',white_result)
    
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break
    
# cv2.release()
cv2.destroyAllWindows()