# -*- coding: utf-8 -*-
"""
Created on Sat Aug 19 14:27:09 2023

@author: Alfy
"""


import pandas as pd
import numpy as np

print("###################################################")

id = [1,2,3,4,5]
names = ["ahmed","mohamed","omar","ali","sssss"]
age = [30,45,45,70,50]
series = pd.Series(index=id , data= age)
print(series)
print("###################################################")

Array1=np.random.randint(3,100,(100,3))
print(Array1)
print("###################################################")
arr_df=pd.DataFrame(Array1,columns=["frist","second","third"],index=(1*i for i in range(100)))
print(arr_df)




df1 = pd.read_csv('50_startups.csv')
df2 = pd.read_csv('kc_house_data.csv')
print(df1.head(5))
print(df1.describe().round())
print("###################################################")
print(df1[1:4])
print("###################################################")
print(df1.iloc[0:2,3])  # to select a particular cell of the dataset using this index

print("###################################################")
def AddstateToState(s):   #function to add City to the end of all states
  return s+str(" State")

result = df1["State"].apply(AddstateToState)
print(result)
print("###################################################")
print(df1["State"])

#-------------------------------------------------
filesMerge = pd.concat([df1,df2],axis=1)
print("###################################################")
print(filesMerge)

print("###################################################")
print([(df1.Administration<136897.80)])

df3 = df1.set_index("Administration")
print("###################################################")
print(df3)
