# This file has hand detection function

import cv2
import numpy as np

def detect_hand(frame, min_YCrCb, max_YCrCb):
    # Convert frame to YCrCb
    imageYCrCb = cv2.cvtColor(frame,cv2.COLOR_BGR2YCR_CB)

    # Find region with skin tone in YCrCb image
    skinRegion = cv2.inRange(imageYCrCb,min_YCrCb,max_YCrCb)

    # Morphological Transformations
    kernel = np.ones((2,2),np.uint8)
    openingFilter = cv2.morphologyEx(skinRegion, cv2.MORPH_OPEN, kernel)

    # Do contour detection on skin region
    contours, hierarchy = cv2.findContours(openingFilter, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for i, c in enumerate(contours):

        area = cv2.contourArea(c)

        if area > 10000:
            # cv2.drawContours(frame, contours, i, (0, 255, 0), 3)
            cnt = max(contours, key=lambda x: cv2.contourArea(x))
            hull = cv2.convexHull(cnt, returnPoints=False)
            defects = cv2.convexityDefects(cnt, hull)

            # Create rectangle around contours
            cx, cy, cw, ch = cv2.boundingRect(cnt)
            cv2.rectangle(frame, (cx, cy), (cx+cw, cy+ch), (0, 255, 255), 2)

            # Extreme Points
            topmost = tuple(cnt[cnt[:, :, 1].argmin()][0])
            cv2.circle(frame, topmost, 10, [54, 38, 227], -1)

            for i in range(defects.shape[0]):
                s, e, f, d = defects[i, 0]
                start = tuple(cnt[s][0])
                end = tuple(cnt[e][0])
                far = tuple(cnt[f][0])
                cv2.line(frame, start, end, [51, 0, 29], 2)

            return topmost
