# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 10:30:39 2023

@author: ellah
"""










import numpy as np
import pandas as pd


# student = ({"id":[1,2,3,4,5],
#             "names":["mahmoud","abdo","ahmed","omar","amr"],
#             "age":[20,30,40,50,60]})
# print (student)
# df = pd.DataFrame(student)
# print (df)
print("__________________________________")















# id = [1,2,3,4,5]
# names = ["mohamed","ahmed","is","os","cs"]
# age = [20,40,60,80,70]
# series = pd.Series(index=id , data= names)
# print(series)
# print("__________________________________")
# arr = np.random.randint(5,100,(100,3))
# arr1=pd.DataFrame(arr,columns=["first","seconed","third"], index=[2*i for i in range(100)])
# print(arr1)
print("__________________________________")
df1 = pd.read_csv('50_startups.csv')
print(df1.head(5))
print(df1.describe().round())
print("__________________________________")

print(df1.iloc[0:3,1])
print(df1.loc[[0,2,5],["State","Profit"]])

print("__________________________________")

df1.sort_values(by="Administration")

df1 = pd.read_csv('50_startups.csv')
df2=pd.read_csv('saved_files/50_Startups_update.csv')
data = pd.concat([df1,df2],axis=1)
print(data)
print("__________________________________")

# df3 = df2.set_index("sex")
# print (df3)
# print("__________________________________")