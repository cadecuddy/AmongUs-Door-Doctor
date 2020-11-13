import cv2 as cv
import numpy as np
'''
MADE BY TEVIN
YOUTUBE: https://www.youtube.com/channel/UCv6Nd7YMrJRDsEo5PVN0scw
'''

def findSwitchPositions(switch_pic_path, base_img, threshold):

    switch_img = cv.imread(switch_pic_path, cv.IMREAD_UNCHANGED)
    switch_w = switch_img.shape[1]
    switch_h = switch_img.shape[0]

    #OPENCV finding matches for the switch_img inside door_img
    method = cv.TM_CCOEFF_NORMED
    result = cv.matchTemplate(base_img, switch_img, method)

    #filtering the results by confidence to remove inaccuracies
    locations = np.where(result >= threshold)
    locations = list(zip(*locations[::-1]))

    rectangles = []
    for loc in locations:
        rect = [int(loc[0]), int(loc[1]), switch_w, switch_h]
        rectangles.append(rect)
        rectangles.append(rect)

    #removing duplicate rectangles/points
    rectangles, weights = cv.groupRectangles(rectangles, 1, 0.2)
    cv.imwrite("results1/test1.jpg",result)
    points = []
    if len(locations):
        #drawing lines for cv.imshow() purposes
        line_color = (0,255,0)
        line_type = cv.LINE_4

        for (x, y, w, h) in rectangles:
            #calculating center points of rectangles
            if switch_pic_path == "light_off.jpg":
                center_x = x + int(w / 2)
                center_y = y + int(h / 2) - 30
            else:
                center_x = x + int(w/2)
                center_y = y + int(h/2)
            #measurements for drawing rectangles (relevant to cv.imshow())
            top_left = (x,y)
            bottom_right = (x + w, y + h)
            cv.rectangle(base_img, top_left, bottom_right, line_color, line_type)
            #adding mouse click points to points array output
            points.append((center_x, center_y))


    else:
        return -1
    #list of 4 x,y points for mouse to click
    return points
