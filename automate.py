import pyautogui as gui
import pytesseract
import time
from scrollsAndClicks import *

Typing_Boult = (10, 285, 1325, 35)   # on maximised mode over 1366*768 screen size 
code = (100, 200, 874, 17)
in_web = (355, 500, 515, 75)

def capture(region):
    img = gui.screenshot(region=region)  # X1,Y1,X2,Y2 Screenshot Capturing according to Cordinates
    # im.save('screenshot.png') # Screenshot saved in this file
    return img 

def pridict(img):
    text = str(pytesseract.image_to_string(img)) # Fetching text from screenshot and passed in text variable
    return text

def write_text(text):
    gui.write(text) # automatically types the text after clicking on the page where to click bottons
    # print(text) # fetched text from screenshot, print on the console


time.sleep(3)

gui.click(CHROME)
time.sleep(2)

gui.click(TPYING_WINDOW)
time.sleep(1)

for _ in range(RUN_N_TIMES):
    
    click_n_times(SCROLLER_BAR_UP)
    time.sleep(.25)

    gui.click(PRACTICE_BOTTON)
    time.sleep(PRAC_LOAD_TIME)

    img = capture(Typing_Boult)
    text = pridict(img)
    # print(text)

    gui.click(KEYBOARD)
    time.sleep(.25)

    write_text(text)
    time.sleep(.25)
    
gui.alert(f'Did {RUN_N_TIMES} times, Wow you made it!!')
