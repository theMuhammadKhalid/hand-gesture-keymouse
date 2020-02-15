# This file has mouse events control functions

import pyautogui as pai

# Find screen width and height
sw, sh = pai.size()

def setCursorPos(tmep, pcp):

    cp = [0,0]

    if abs(tmep[0]-pcp[0]) < 40 and abs(tmep[1]-pcp[1]) < 40:
        cp[0] = pcp[0]
        cp[1] = pcp[1]
    else:
        cp[0] = tmep[0]
        cp[1] = tmep[1]

    if cp[0] > sw:
        cp[0] = sw - 1

    if cp[1] > sh:
        cp[1] = sh - 1

    return cp

# end setCursorPos function

def moveCursor(frame, tmep):

    # Cursor movement
    pai.FAILSAFE = False          
    mcx, mcy = setCursorPos(tmep, pai.position())
    pai.moveTo(mcx*2, mcy*2, duration = 0.20)

# end moveCursor function
