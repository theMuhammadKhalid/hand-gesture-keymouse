# This file has Alphabets Keys Interface functions

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
    frame = cv2.rectangle(frame, (3,360), (637,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 18).getsize("Select Alphabets for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/a.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("A")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/b.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("B")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw image 3
    s_img = cv2.imread("./Images/c.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,167:167+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (165,380), (sw+165+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("C")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (164,366), (164+bw,366+bh), (0,0,0), -1)

    # draw image 4
    s_img = cv2.imread("./Images/d.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,246:246+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (244,380), (sw+244+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("D")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (243,366), (243+bw,366+bh), (0,0,0), -1)

    # draw image 5
    s_img = cv2.imread("./Images/e.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,325:325+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (323,380), (sw+323+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("E")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (322,366), (322+bw,366+bh), (0,0,0), -1)

    # draw image 6
    s_img = cv2.imread("./Images/f.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,404:404+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (402,380), (sw+402+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("F")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (401,366), (401+bw,366+bh), (0,0,0), -1)

    # draw image 7
    s_img = cv2.imread("./Images/g.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,483:483+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (481,380), (sw+481+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("G")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (480,366), (480+bw,366+bh), (0,0,0), -1)

    # draw image 8
    s_img = cv2.imread("./Images/h.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,562:562+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (560,380), (sw+560+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("H")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (559,366), (559+bw,366+bh), (0,0,0), -1)

    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "A"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "B"
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    guided_text_3 = "C"
    draw.text((167, 368), guided_text_3, font = font, fill = (255,255,255))

    guided_text_4 = "D"
    draw.text((245, 368), guided_text_4, font = font, fill = (255,255,255))

    guided_text_5 = "E"
    draw.text((324, 368), guided_text_5, font = font, fill = (255,255,255))

    guided_text_6 = "F"
    draw.text((403, 368), guided_text_6, font = font, fill = (255,255,255))

    guided_text_7 = "G"
    draw.text((482, 368), guided_text_7, font = font, fill = (255,255,255))

    guided_text_8 = "H"
    draw.text((561, 368), guided_text_8, font = font, fill = (255,255,255))

    title_guided_text = "Select Alphabets for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 18)
    draw.text((4, 342), title_guided_text, font = font, fill = (0,0,0))

    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    return frame

def drawGuide_2(frame):
    
    # draw outline
    frame = cv2.rectangle(frame, (3,360), (637,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 18).getsize("Select Alphabets for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/i.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("I")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/j.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("J")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw image 3
    s_img = cv2.imread("./Images/k.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,167:167+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (165,380), (sw+165+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("K")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (164,366), (164+bw,366+bh), (0,0,0), -1)

    # draw image 4
    s_img = cv2.imread("./Images/l.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,246:246+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (244,380), (sw+244+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("L")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (243,366), (243+bw,366+bh), (0,0,0), -1)

    # draw image 5
    s_img = cv2.imread("./Images/m.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,325:325+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (323,380), (sw+323+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("M")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (322,366), (322+bw,366+bh), (0,0,0), -1)

    # draw image 6
    s_img = cv2.imread("./Images/n.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,404:404+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (402,380), (sw+402+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("N")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (401,366), (401+bw,366+bh), (0,0,0), -1)

    # draw image 7
    s_img = cv2.imread("./Images/o.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,483:483+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (481,380), (sw+481+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("O")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (480,366), (480+bw,366+bh), (0,0,0), -1)

    # draw image 8
    s_img = cv2.imread("./Images/p.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,562:562+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (560,380), (sw+560+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("P")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (559,366), (559+bw,366+bh), (0,0,0), -1)

    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "I"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "J"
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    guided_text_3 = "K"
    draw.text((167, 368), guided_text_3, font = font, fill = (255,255,255))

    guided_text_4 = "L"
    draw.text((245, 368), guided_text_4, font = font, fill = (255,255,255))

    guided_text_5 = "M"
    draw.text((324, 368), guided_text_5, font = font, fill = (255,255,255))

    guided_text_6 = "N"
    draw.text((403, 368), guided_text_6, font = font, fill = (255,255,255))

    guided_text_7 = "O"
    draw.text((482, 368), guided_text_7, font = font, fill = (255,255,255))

    guided_text_8 = "P"
    draw.text((561, 368), guided_text_8, font = font, fill = (255,255,255))

    title_guided_text = "Select Alphabets for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 18)
    draw.text((4, 342), title_guided_text, font = font, fill = (0,0,0))

    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    return frame

def drawGuide_3(frame):
    
    # draw outline
    frame = cv2.rectangle(frame, (3,360), (637,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 18).getsize("Select Alphabets for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/q.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Q")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/r.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("R")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw image 3
    s_img = cv2.imread("./Images/s.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,167:167+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (165,380), (sw+165+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("S")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (164,366), (164+bw,366+bh), (0,0,0), -1)

    # draw image 4
    s_img = cv2.imread("./Images/t.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,246:246+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (244,380), (sw+244+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("T")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (243,366), (243+bw,366+bh), (0,0,0), -1)

    # draw image 5
    s_img = cv2.imread("./Images/u.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,325:325+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (323,380), (sw+323+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("U")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (322,366), (322+bw,366+bh), (0,0,0), -1)

    # draw image 6
    s_img = cv2.imread("./Images/v.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,404:404+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (402,380), (sw+402+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("V")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (401,366), (401+bw,366+bh), (0,0,0), -1)

    # draw image 7
    s_img = cv2.imread("./Images/w.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,483:483+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (481,380), (sw+481+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("W")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (480,366), (480+bw,366+bh), (0,0,0), -1)

    # draw image 8
    s_img = cv2.imread("./Images/x.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,562:562+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (560,380), (sw+560+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("X")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (559,366), (559+bw,366+bh), (0,0,0), -1)

    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "Q"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "R"
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    guided_text_3 = "S"
    draw.text((167, 368), guided_text_3, font = font, fill = (255,255,255))

    guided_text_4 = "T"
    draw.text((245, 368), guided_text_4, font = font, fill = (255,255,255))

    guided_text_5 = "U"
    draw.text((324, 368), guided_text_5, font = font, fill = (255,255,255))

    guided_text_6 = "V"
    draw.text((403, 368), guided_text_6, font = font, fill = (255,255,255))

    guided_text_7 = "W"
    draw.text((482, 368), guided_text_7, font = font, fill = (255,255,255))

    guided_text_8 = "X"
    draw.text((561, 368), guided_text_8, font = font, fill = (255,255,255))

    title_guided_text = "Select Alphabets for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 18)
    draw.text((4, 342), title_guided_text, font = font, fill = (0,0,0))

    frame = cv2.cvtColor(np.array(pil_img), cv2.COLOR_RGB2BGR)
    
    return frame

def drawGuide_4(frame):
    
    # draw outline
    frame = cv2.rectangle(frame, (3,360), (163,475), (255,255,255), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Select Alphabets for ")[0] + 5
    bh = 19 # fixed
    frame = cv2.rectangle(frame, (2,340), (2+bw,340+bh), (255,255,255), -1)

    # draw image 1
    s_img = cv2.imread("./Images/y.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,10:10+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (8,380), (sw+8+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Y")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (7,366), (7+bw,366+bh), (0,0,0), -1)

    # draw image 2
    s_img = cv2.imread("./Images/z.jpg")    
    sw = s_img.shape[1]
    sh = s_img.shape[0]           
    frame[381:381+sh,88:88+sw] = s_img
    # draw outline
    frame = cv2.rectangle(frame, (86,380), (sw+86+2,sh+380+2), (0,0,0), 2)
    # draw horizontal bar
    bw = ImageFont.truetype("./Fonts/Helvetica.ttf", 14).getsize("Z")[0] + 5
    bh = 13 # fixed
    frame = cv2.rectangle(frame, (85,366), (85+bw,366+bh), (0,0,0), -1)

    # draw text    
    pil_img = Image.fromarray(cv2.cvtColor(frame,cv2.COLOR_BGR2RGB) )   
    draw = ImageDraw.Draw(pil_img)
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
    
    guided_text_1 = "Y"
    draw.text((9, 368), guided_text_1, font = font, fill = (255,255,255))

    guided_text_2 = "Z"
    draw.text((87, 368), guided_text_2, font = font, fill = (255,255,255))

    title_guided_text = "Select Alphabets for "
    font = ImageFont.truetype("./Fonts/Helvetica.ttf", 14)
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
    elif fc > 400 and fc <= 600:
        frame = drawGuide_3(frame)
        fc = fc + 1
    elif fc > 600 and fc <= 800:
        frame = drawGuide_4(frame)
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

