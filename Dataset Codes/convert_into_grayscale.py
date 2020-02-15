import cv2
import os

i = 1

for filename in os.listdir("path\\to\\folder\\of\\images\\"):
    image = cv2.imread("path\\to\\folder\\of\\images\\"+filename)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite("path\\to\\folder\\for\\saving\\images\\image_name_"+str(i)+".jpg",gray)
    print(i)
    i += 1

  
cv2.waitKey(0)
cv2.destroyAllWindows()
