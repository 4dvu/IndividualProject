import cv2
import math
import numpy as np
from matplotlib import pyplot as plt


img = cv2.imread('bbox/3m/bbox3_44.png')

def ROI(image):
    xsys = 234.5 
    imgray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(imgray, 127, 255, 0)
    contours, _ = cv2.findContours(thresh, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    if contours != []:
        areas = [cv2.contourArea(c) for c in contours]
        maxIndex = np.argmax(areas)
        cnt = contours[maxIndex] 
        x,y,w,h = cv2.boundingRect(cnt)
        cv2.rectangle(imgray, (x,y), (x+w, y+h), (255,0,0), 2)
        cv2.imshow('img',imgray)
        # to visualize bounding box
        cv2.waitKey()             
        cv2.destroyAllWindows()
        xT_centre = x + w/2
        D = 3 # disance from the occupant to the system
        if xT_centre < xsys:
            delta_x = (xsys - xT_centre)*5/469
            angle_radiant = math.atan((delta_x)/D)
            angle_degree = (angle_radiant*180)/math.pi
        else:
            delta_x = (xT_centre - xsys)*5/469
            angle_radiant = -math.atan((delta_x)/D)
            angle_degree = (angle_radiant*180)/math.pi
    return angle_degree
print(ROI(img))