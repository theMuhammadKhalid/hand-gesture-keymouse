# Test drive for Numbers

import cv2
import tensorflow as tf
import logging
tf.get_logger().setLevel(logging.ERROR)

import numeric_keys_interface as nki

# Create video capture object
video = cv2.VideoCapture(0)

# Turn the autofocus off
video.set(cv2.CAP_PROP_AUTOFOCUS, 0)

CATEGORIES = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "unknown"]
model = tf.keras.models.load_model("./Models/Numeric-Keys-CNN.model")
fList = []

def prepare(frame):
    IMG_SIZE = 64
    
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    new_array = cv2.resize(gray_img, (IMG_SIZE, IMG_SIZE))
    return new_array.reshape(-1, IMG_SIZE, IMG_SIZE, 1)


nof = 1
fc = 1 # Frame count for guide animation

while True:
    nof = nof + 1
    check, frame = video.read()

    prediction = model.predict([prepare(frame)])
    pList = prediction.tolist()
    predictClass = CATEGORIES[pList[0].index(max(pList[0]))]
    fList.append(str(predictClass))
    
    if len(fList) >= 10:
        repeated = max(set(fList), key = fList.count)
        fList.clear()
        print(repeated)

    nki.drawLogo(frame)
    frame, fc = nki.drawGuide(frame, fc)
    frame = nki.drawText(frame, "Press Q for Exit")
                       
    cv2.imshow("Hand Gesture KeyMouse", frame)

    # Wait until a user press a key
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
    

print("Total number of frames = "+str(nof))
video.release()
cv2.destroyAllWindows()

