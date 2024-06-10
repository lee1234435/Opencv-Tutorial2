import cv2
import numpy as np
import copy

def find_contours_in_color_range(image, lower_range, upper_range):
    # 이미지를 HSV로 변환
    hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # 지정한 색 범위에 해당하는 마스크 생성
    color_mask = cv2.inRange(hsv_image, lower_range, upper_range)

    # 마스크와 원본 이미지 비트와 연산
    masked_image = cv2.bitwise_and(image, image, mask=color_mask)

    # 마스크 이미지를 그레이스케일로 변환
    gray_mask = cv2.cvtColor(masked_image, cv2.COLOR_BGR2GRAY)

    # 이진화 처리
    _, binary_mask = cv2.threshold(gray_mask, 1, 255, cv2.THRESH_BINARY)

    # 윤곽선 찾기
    contours, _ = cv2.findContours(binary_mask, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    # 윤곽선 그리기
    cv2.drawContours(image, contours, -1, (0, 255, 0), 2)

    return image


cap = cv2.VideoCapture("ex8/video.mp4")

while cap.isOpened():
    ret, frame = cap.read()
    
    if not ret:
        break
    
    frame_copy = copy.deepcopy(frame) # 원본 frame 은 건들지 않고 복사본 frame 으로 다루기 위한 용도

    height, width,_ = frame_copy.shape
    roi_height = int(height/3)
    roi_width = int(width/3)

    roi = frame_copy[2*roi_height: height, roi_width:(width-roi_width)]

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lower_white = np.array([0,0,200],dtype=np.uint8)
    upper_white = np.array([255,30,255],dtype=np.uint8)
    white_mask = cv2.inRange(hsv, lower_white, upper_white)

    white_result1 = cv2.bitwise_and(frame, frame, mask=white_mask)

    white_result2 = find_contours_in_color_range(roi, lower_white, upper_white)

    cv2.imshow("Original", frame)
    cv2.imshow("White", white_result1)
    cv2.imshow("edge_roi", white_result2)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        break

# cv2.release()

cv2.destroyAllWindows()