import numpy as np
import cv2

class Pen_Detector:

    def __init__(self, lower, upper):
        self.lower = lower
        self.upper = upper
    
    def detect(self, frame):
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, self.lower, self.upper)
        mask = cv2.erode(mask, np.ones((5, 5), np.uint8), iterations = 3)
        mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, np.ones((5, 5), np.uint8))
        mask = cv2.dilate(mask, np.ones((5, 5), np.uint8), iterations = 1)
        result = cv2.bitwise_and(frame, frame, mask = mask)

        cnts, heir = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2:]

        center, radius = None, 0
        if len(cnts) > 0:
            c = max(cnts, key = cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            center = (int(M['m10'] / M['m00']), int(M['m01'] / M['m00'])) if radius > 5 else None

        return result, mask, center, radius