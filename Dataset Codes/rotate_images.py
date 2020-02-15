import cv2
import os
from scipy import ndimage

i = 0

for filename in os.listdir("path\\to\\folder\\of\\images\\"):
    img = cv2.imread("path\\to\\folder\\of\\images\\"+filename)

    rotated = ndimage.rotate(img, 270)
    
    cv2.imwrite("path\\to\\folder\\for\\saving\\images\\"+filename, rotated)
    print(i)
    i += 1

  
cv2.waitKey(0)
cv2.destroyAllWindows()
