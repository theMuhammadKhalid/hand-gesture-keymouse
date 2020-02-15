# Resize Images

import cv2
import os

i = 0

for filename in os.listdir("path\\to\\folder\\of\\images\\"):
    
    image = cv2.imread("path\\to\\folder\\of\\images\\"+filename)

    # resize width and height
    width = 100
    height = 100
    
    resized = cv2.resize(image, (width,height))

    cv2.imwrite("path\\to\\folder\\for\\saving\\images\\"+filename,resized)

    print(i)
    i += 1








