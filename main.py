'''
MADE BY TEVIN
YOUTUBE: https://www.youtube.com/channel/UCv6Nd7YMrJRDsEo5PVN0scw
'''
import cv2 as cv
import numpy as np
from locator import findSwitchPositions
import pyautogui
from PIL import ImageGrab
import keyboard
from time import sleep
pyautogui.PAUSE = 0.05
tasks = ['door_switch.jpg', 'light_off.jpg']

def click(list):
    for pt in list:
        #autoclicking of door switches
        pyautogui.moveTo(pt[0],pt[1])
        pyautogui.click()

def detect():
    sleep(.35) #allows task panel to fully open to prevent inaccuracy
    screenshot = ImageGrab.grab()
    screenshot = np.array(screenshot)
    screenshot = cv.cvtColor(screenshot,cv.COLOR_RGB2BGR)
    #give spotter value of -1 by default
    spotter = findSwitchPositions('dog.jpg',screenshot,0.85)
    c = 0
    while spotter == -1 and c < len(tasks):
        spotter = findSwitchPositions(tasks[c], screenshot, 0.85)
        c += 1
    if spotter != -1:
        click(spotter)
        pyautogui.press("esc")

def runBot():
    while True:
        key = keyboard.read_key()
        if key == "e":
            detect()
        if key == "`":
            exit()

print("WELCOME TO Tevin's Door Tool V1!\n")
print("Right now it ONLY supports 1920x1080\n")
print("door tool: ACTIVE\n")
print("_____________________________________\n")
print("PRESS ~ TO QUIT Tevin's Door Tool")
runBot()