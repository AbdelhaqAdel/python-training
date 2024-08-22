# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 11:40:44 2023

@author: Alfy
"""


import cv2
import numpy as np
from scipy import ndimage

new=cv2.imread("image1.jpg")
#flip=np.fliplr(img)
# new=cv2.imwrite("flipimg.jpg",flip)
# print(new)



# cc=ndimage.median_filter(img,3)
# ccTest=cv2.imwrite("median.jpg",cc)
# print(ccTest)

# gus=ndimage.gaussian_filter(img,3)
# gusTest=cv2.imwrite("gussian.jpg",gus)
# print(gusTest)


# sb=ndimage.sobel(img,axis=1)
# sbTest=cv2.imwrite("sob.jpg",sb)
# print(sbTest)





# flipup=np.flipup(img)
# flipupimg=cv2.imwrite("flipup.jpg",flipup)
# print(flipupimg)
#create a calculator

# input_str = input()
# inputs = input_str.split()  # Split by default whitespace characters

# a = int(inputs[0])
# s = inputs[1]
# b = int(inputs[2])
# if s=="+":
#     print (a + b)
# elif s=="-":
#     print (a - b)
# elif s=="*":
#     print (a * b)
# else:
#     print(int(a/b))
    
    
    
#----------------------------------------------------------------------
#another solution    
#expression = input("Enter a mathematical expression (e.g., 5+6): ")
#print(eval(expression))
    






