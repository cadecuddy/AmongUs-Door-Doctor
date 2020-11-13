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
tasks = ['door_switch.jpg', 'light_off.jpg', 'blue_wire.jpg']

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

    # Ugly repetitive "IF" statements but run quicker than a loop
    spotter = findSwitchPositions(tasks[0], screenshot, 0.85)
    if spotter != -1: click(spotter), pyautogui.press("esc")
    spotter = findSwitchPositions(tasks[1], screenshot, 0.85)
    if spotter != -1: click(spotter), pyautogui.press("esc")
    spotter = findSwitchPositions(tasks[2], screenshot, 0.85)
    if spotter != -1: fix_wires(spotter)

def fix_wires(positions):
    # TODO: ADD WIRES CODE
    return -1

def panic():
    pyautogui.moveTo(1788,709)
    pyautogui.click()

def runBot():
    panic_mode = False
    while True:
        key = keyboard.read_key()
        if key == "e":
            detect()
        if key == "p" and panic_mode == False:
            panic_mode = True
            panic()
        else:
            panic_mode = False
        if key == "`":
            exit()

print("WELCOME TO Tevin's Door Tool V1!\n")
print("Right now it ONLY supports 1920x1080\n")
print("door tool: ACTIVE\n")
print("_____________________________________\n")
print("PRESS ~ TO QUIT Tevin's Door Tool")
runBot()