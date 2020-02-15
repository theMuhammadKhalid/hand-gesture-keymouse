# This file has Mouse Interface functions

import cv2
import numpy as np 
from PIL import Image, ImageFont, ImageDraw

def drawLogo(frame):
    logo_img = cv2.imread("./Images/logo.png",-1)    
    lw = logo_img.shape[1]
    lh = logo_img.shape[0]
    wh,ww,wc = frame.shape   
    y1, y2 = 10, 10+lh
    x1, x2 = ww-lw-10, ww-lw-10+lw
    alpha_s = logo_img[:, :, 3] / 255.0
    alpha_l = 1.0 - alpha_s    
    for c in range(0, 3):
        frame[y1:y2, x1:x2, c] = (alpha_s * logo_img[:, :, c] + alpha_l * frame[y1:y2, x1:x2, c])

def drawGuide(frame):
    
    # draw outline
    frame = cv2.rectangle(frame, (3,360), (321,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 18).getsize("Select for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/move.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Move")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/double.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 12).getsize("Double click")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw image 3
    s_img = cv2.imread("./Images/left.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,167:167+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (165,380), (sw+165+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Left click")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (164,366), (164+bw,366+bh), (0,0,0), -1)

    # draw image 4
    s_img = cv2.imread("./Images/right.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,246:246+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (244,380), (sw+244+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Right click")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (243,366), (243+bw,366+bh), (0,0,0), -1)

    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "Move"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "Double click"
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 12)
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    guided_text_3 = "Left click"
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    draw.text((167, 368), guided_text_3, font = font, fill = (255,255,255))

    guided_text_4 = "Right click"
    draw.text((245, 368), guided_text_4, font = font, fill = (255,255,255))

    title_guided_text = "Select for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 18)
    draw.text((4, 342), title_guided_text, font = font, fill = (0,0,0))

    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    return frame

def drawText(frame, text):
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    draw.text((10, 10), str(text), font = font, fill = (0,0,255))
    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)   
    return frame
