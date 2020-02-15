from PIL import Image
import os

i = 1

for filename in os.listdir("path\\to\\folder\\of\\images\\"):
    
    img = Image.open("path\\to\\folder\\of\\images\\"+filename)
    img.save("path\\to\\folder\\for\\saving\\images\\image_name_"+str(i)+".jpg")
    
    
    print(i)
    i += 1

  
