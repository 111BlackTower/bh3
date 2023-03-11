import pyautogui
import time
from pynput.mouse import Listener


def mouseListener(on_click):
    with Listener(on_click=on_click) as listener:
        listener.join()

def on_click(x, y, button, pressed):
    global a
    b = time.time() - a
    if b > 0.18:
        x, y = pyautogui.position()
        rgb = pyautogui.screenshot().getpixel((x, y))
        posi = 'x,y:' + str(x).rjust(4) + ',' + str(y) + '  RGB:' + str(rgb)
        print(posi)
        print('时间间隔为', b)
        a = time.time()

while True:
    a = time.time()
    mouseListener(on_click)
