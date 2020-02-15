# This file has Numeric Keys Interface functions

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
    
 
def drawGuide_1(frame):
    
    # draw outline
    frame = cv2.rectangle(frame, (3,360), (479,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 18).getsize("Select Numbers for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/0.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("0")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/1.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("1")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw image 3
    s_img = cv2.imread("./Images/2.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,167:167+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (165,380), (sw+165+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("2")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (164,366), (164+bw,366+bh), (0,0,0), -1)

    # draw image 4
    s_img = cv2.imread("./Images/3.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,246:246+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (244,380), (sw+244+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("3")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (243,366), (243+bw,366+bh), (0,0,0), -1)

    # draw image 5
    s_img = cv2.imread("./Images/4.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,325:325+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (323,380), (sw+323+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("4")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (322,366), (322+bw,366+bh), (0,0,0), -1)

    # draw image 6
    s_img = cv2.imread("./Images/5.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,404:404+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (402,380), (sw+402+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("5")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (401,366), (401+bw,366+bh), (0,0,0), -1)


    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "0"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "1"
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    guided_text_3 = "2"
    draw.text((167, 368), guided_text_3, font = font, fill = (255,255,255))

    guided_text_4 = "3"
    draw.text((245, 368), guided_text_4, font = font, fill = (255,255,255))

    guided_text_5 = "4"
    draw.text((324, 368), guided_text_5, font = font, fill = (255,255,255))

    guided_text_6 = "5"
    draw.text((403, 368), guided_text_6, font = font, fill = (255,255,255))

    title_guided_text = "Select Numbers for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 18)
    draw.text((4, 342), title_guided_text, font = font, fill = (0,0,0))

    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    return frame

def drawGuide_2(frame):
    
    # draw outline
    frame = cv2.rectangle(frame, (3,360), (321,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 18).getsize("Select Numbers for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/6.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("6")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/7.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("7")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw image 3
    s_img = cv2.imread("./Images/8.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,167:167+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (165,380), (sw+165+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("8")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (164,366), (164+bw,366+bh), (0,0,0), -1)

    # draw image 4
    s_img = cv2.imread("./Images/9.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,246:246+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (244,380), (sw+244+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("9")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (243,366), (243+bw,366+bh), (0,0,0), -1)

    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "6"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "7"
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    guided_text_3 = "8"
    draw.text((167, 368), guided_text_3, font = font, fill = (255,255,255))

    guided_text_4 = "9"
    draw.text((245, 368), guided_text_4, font = font, fill = (255,255,255))

    title_guided_text = "Select Numbers for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 18)
    draw.text((4, 342), title_guided_text, font = font, fill = (0,0,0))

    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    return frame

def drawGuide(frame, fc):
    if fc <= 200:
        frame = drawGuide_1(frame)
        fc = fc + 1
    elif fc > 200 and fc <= 400:
        frame = drawGuide_2(frame)
        fc = fc + 1
    else:
        fc = 1
        
    return frame, fc

def drawText(frame, text):
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    draw.text((10, 10), str(text), font = font, fill = (0,0,255))
    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)   
    return frame
    
