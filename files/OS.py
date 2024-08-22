# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:59:18 2023

@author: Alfy
"""

import os 
import time
# os.getcwd()
os.chdir("D:/pyhon/files/saved_files/")
print(os.getcwd())

# print(os.listdir("D:/pyhon/files/saved_files"))
# #os.mkdir("D:/pyhon/files/saved_files/xx")
# print(os.listdir("D:/pyhon/files/saved_files"))


# #os.rmdir("D:/pyhon/files/saved_files/xx")
# print(os.listdir("D:/pyhon/files/saved_files"))

# os.rename("D:/pyhon/files/saved_files/xx", "D:/pyhon/files/saved_files/newfile")
# print(os.listdir("D:/pyhon/files/saved_files"))

# print(os.stat("D:/pyhon/files/saved_files/ww.txt"))
# print(time.ctime(1694460540))


#print(os.cpu_count())


#print(os.get_exec_path())

#print(os.getpid())
#os.getppid()

print(os.path.abspath('D:/pyhon/files/saved_files/ww.txt'))


#file=open("D:/pyhon/files/saved_files/ww.txt","w")
#file.write("ssss")

file=open("D:/pyhon/files/saved_files/ww.txt","r")
print(file.readline())
# print(file.writable())
# file.close()