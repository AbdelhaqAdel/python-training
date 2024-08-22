# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 22:05:44 2023

@author: Alfy
"""

#import matplotlib.pyplot as plt
import numpy as np
import cv2
print("////////////////////////")
img=cv2.imread("image1.jpg")
print(img.shape)

# cam = cv2.VideoCapture("video2.mp4")
# while True:
#     ret,frame = cam.read()
#     xxx = cv2.resize(frame,(200,200))
#     xx = cv2.cvtColor(xxx,cv2.COLOR_RGB2GRAY)
#     cv2.imshow("video2.mp4", xx)
    
    
#     if cv2.waitKey(1) & 0xff ==ord("q"):
#         break