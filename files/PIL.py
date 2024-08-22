# -*- coding: utf-8 -*-
"""
Created on Thu Sep  7 20:06:43 2023

@author: Alfy
"""

from PIL import Image
img=Image.open('image1.jpg')
print(img)
img.show()
print(img.format)
print(img.mode)   
print(img.size)


small =img.resize((500,300))
print(small.size)
small.save("saved_files/small.jpg")
#small.show()



# img.thumbnail((200,500))   #عشان الصوره متبوظش
# print(img.size)



cropped=img.crop((0,0,500,500))
cropped.save("saved_files/cropped.jpg")
#cropped.show()

img_90=img.rotate(90,expand=True)
img_90.save("saved_files/rotate.jpg")
#img_90.show()

img_flip=img.transpose(Image.FLIP_TOP_BOTTOM)
img_flip.save("saved_files/Flip.jpg")
#img_flip.show()


grey=img.convert("L")
grey.save("saved_files/grey.jpg")
#grey.show()


