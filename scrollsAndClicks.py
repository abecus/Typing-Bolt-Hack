import pyautogui as gui


CHROME = (515, 750)     # chrom icone in taskbar
TPYING_WINDOW = (30, 15)        # typing bolt window
KEYBOARD = (660, 380)       # it's keybord (vertual), only wheres no keys like upper band
SCROLLER_BAR_UP = (1357, 90)        # scroll bar  for scrolling (bit lower than up arrow)
SCROLLER_BAR_DOWN = (1357, 693)     # scroll bar  for scrolling (bit higher than down arrow) 
PRACTICE_BOTTON = (770, 130)        # practice botton
PRAC_LOAD_TIME = 6         # in seconds, you might want to change it as your convinient internet speed just do try and error nethod
RUN_N_TIMES = 100           # how much times you want to run it


def click_n_times(coord, n=10):
    '''
    coord takes an tuple of type, (x,y)
    '''
    gui.mouseUp()
    for _ in range(n):
        gui.click(coord)
    gui.mouseUp()
