# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:39:12 2023

@author: Alfy
"""
from skimage.util.dtype import img_as_ubyte
from skimage import io
import numpy as np
import cv2
img= io.imread("image1.jpg")
# noncut_image=cv2.imread("saved_files/cuting.jpg")

print(type(img))

#img=img_as_ubyte(img)

print(img[10:100,0:50])
# cut_image=cv2.imwrite("saved_files/cuting.jpg",noncut_image)
# cut_image.show()


max_value=img.max()
print(max_value)
print(max_value)

mean=img.mean()
print(mean)

imge=cv2.imread("saved_files/cuting.jpg")
flip_L_R=np.fliplr(imge)
flip_L_R.save("saved_files/flip_l_r.jpg")
flip_L_R.show()