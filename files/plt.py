# -*- coding: utf-8 -*-
"""
Created on Wed Aug 23 20:08:45 2023

@author: Alfy
"""

#to make visulization for data

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


age= [20, 22, 25, 30, 50]
salary=[1000, 2000, 2500, 4000, 7000]
plt.title("Age VS Salary")
plt.xlabel("Age")
plt.ylabel("Salary")
#print(plt.plot(age, salary,color="yellow"))

age_1= [20, 22, 25, 30, 50]
salary_1=[1000, 2000, 3000, 4000, 5000]

print("///////////////////////////////")
age_2= [20, 22, 25, 30, 50]
salary_2=[1500, 2500, 3500, 4500, 5500]


age_3= [20, 22, 25, 30, 50]
salary_3=[3000, 6000, 9000, 10000, 12000]

# plt.title("Age VS Salary")
# plt.xlabel("Age")
# plt.ylabel("Salary")
# plt.plot(age_1, salary_1,color="red",
#          label="first group",marker="o",
#          linestyle="--")
# plt.plot(age_2, salary_2,color="blue",
#          marker="o",label="second group",
#          linestyle=":")

# plt.legend()

# plt.savefig("pltimage.jpg")

# plt.grid()




#-----------------second type---------------

width=0.3
x=np.arange(len(age_1))
plt.grid()

plt.bar(x-width,salary_1,width=width,color="red")
plt.bar(x,salary_2,width=width,color="blue")
plt.bar(x+width,salary_3,color="yellow",width=width)

plt.grid()


plt.savefig("33pltimage.jpg")

#-----------------third type---------------

# age_4= ["hr", "it","a", "b", "c"]
# salary_4=[1000, 2000, 3000, 4000, 5000]
# color=["red","yellow","orange","green","purple"]
# c=[0,0,0,0,0.3]
# plt.pie(salary_4,labels=age_4)
# plt.show()
# plt.pie(salary_4,labels=age_4,startangle=90,explode=c,colors=color)
# plt.show()

#import matplotlib.pyplot as plt

# age = [20, 22, 25, 30, 50]
# salary = [1000, 2000, 2500, 4000, 7000]

# plt.title("Age Vs. Salary")
# plt.xlabel("\nAge")
# plt.ylabel("Salary\n")
# plt.plot(age, salary, color = 'yellow')