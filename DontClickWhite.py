from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con

time.sleep(2)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#color of center : (225, 219, 195)
startx, starty = pyautogui.position()
print("MOVE")
time.sleep(2)
endx, endy = pyautogui.position()
print("done")

pic = pyautogui.screenshot(region = ((startx, starty, endx - startx, endx - startx)))
width, height = pic.size

cords = []
for i in range(0, 4):
    cords.append([])
    for k in range(0, 4):
        cords[i].append([])
        cords[i][k].append(i * width//4)
        cords[i][k].append(k * height//4)

while keyboard.is_pressed('q') == False:
    #pic = pyautogui.screenshot(region = ((startx, starty, endx - startx, endx - startx)))
    for i in range(len(cords)):
        pic = pyautogui.screenshot(region = ((startx, starty, endx - startx, endx - startx)))
        for k in range(len(cords[i])):
            r, g, b = pic.getpixel((cords[i][k][0], cords[i][k][1]))
            if(g == 0):
                click(cords[i][k][0] + startx, cords[i][k][1] + starty)
                time.sleep(0.01)
                break
                
