import numpy as np
import cv2, pyautogui, time
from utils.Pen_Detector import *


LOWER_GREEN = np.array([36, 25, 25])
UPPER_GREEN = np.array([70, 255, 255])

pen_detetctor = Pen_Detector(LOWER_GREEN, UPPER_GREEN)

cap = cv2.VideoCapture(0)

cap.set(cv2.CAP_PROP_FRAME_WIDTH, 1920)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 1080)

time.sleep(5)

while True:
    _, frame = cap.read()
    frame = cv2.flip(frame, 1)
    result, mask, center, radius = pen_detetctor.detect(frame)
    if center != None:
        cv2.circle(frame, center, int(radius), (255, 0, 0), 2)
        pyautogui.moveTo(center[0], center[1])
    # cv2.imshow('Frame', frame)
    # cv2.imshow('Mask', mask)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()
cv2.destroyAllWindows()