# Test drive for Mouse

import cv2
import numpy as np
import handDetection as hde
import mouse_interface as mi
import mouse_events_control as mec
import pyautogui as pai
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)

# Create video capture object
video = cv2.VideoCapture(0)

# turn the autofocus off
video.set(cv2.CAP_PROP_AUTOFOCUS, 0)

CATEGORIES = ["move", "double", "left", "right", "unknown"]
model = tf.keras.models.load_model("./Models/Mouse-CNN.model")
fList = []

def prepare(frame):
    IMG_SIZE = 64
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    new_array = cv2.resize(gray_img, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


# Constants for finding range of skin color in YCrCb
min_YCrCb = np.array([0,133,77],np.uint8)
max_YCrCb = np.array([255,173,127],np.uint8)

nof = 1
while True:
    nof = nof + 1
    check, frame = video.read()

    tmep = hde.detect_hand(frame, min_YCrCb, max_YCrCb)

    prediction = model.predict([prepare(frame)])
    pList = prediction.tolist()
    predictClass = CATEGORIES[pList[0].index(max(pList[0]))]
    fList.append(str(predictClass))
    
    if len(fList) >= 10:
        repeated = max(set(fList), key = fList.count)
        fList.clear()
        print(repeated)

        if tmep is None:
            pass
        else:
            if repeated == "move":
                mec.moveCursor(frame, tmep)
            elif repeated == "double":
                pai.doubleClick()
            elif repeated == "left":
                pai.click(button='left')
            elif repeated == "right":
                pai.click(button='right')
            else:
                pass   
    
            
    mi.drawLogo(frame)
    frame = mi.drawGuide(frame)
    frame = mi.drawText(frame, "Press Q for Exit")
    
    cv2.imshow("Hand Gesture KeyMouse", frame)

    # Wait until a user press a key
    key = cv2.waitKey(1)
    if key == ord('q'):
        break

print("Total number of frames = "+str(nof))
video.release()
cv2.destroyAllWindows()
