# -*- coding: utf-8 -*-
"""
Created on Tue Aug 15 12:26:59 2023

@author: Alfy
"""
#calc the age using days
import pandas as pd
import numpy as np



Array1=np.random.randint(3,100,(100,4))
print(Array1)
print("###################################################")
arr_df=pd.DataFrame(Array1,columns=["frist","second","third","fourth"],index=(1*i for i in range(100)))
print(arr_df)





x=int(input("enter your age :"))
years=int(x/365)
print("years : ",years)
res=int(x-(years*365))
months=int((res/30))
print("months : ",months)
print("days : ",int(res-months*30))
