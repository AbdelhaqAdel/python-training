# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 22:48:37 2023

@author: Alfy
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
print("////////////////////////////////////")

tips=sns.load_dataset("ss")
print(tips.head(5))
print("////////////////////////////////////")

#-----------------first type of seaborn style----------------------------

# fmri= sns.load_dataset("fmri")
# print(fmri.head(5))

# plt.figure(figsize=(5,5))
# sns.set_style('darkgrid')
# sns.lineplot(x="timepoint",y="signal",data=fmri,style="region")
# plt.title("yeaars vs pass")
# #-----------------second type of seaborn style----------------------------
# flights=sns.load_dataset('flights')
# print(flights.head())


# x_fd=flights[flights["month"]=="Feb"]
# sns.set_style("darkgrid")
# sns.lineplot(x="year",y="passengers",data=flights,hue="month")
# plt.title("Years VS passengers")
# plt.xlabel("years")
# plt.ylabel("passengers")
#------------------------------------------------

#-----------------third type of seaborn style----------------------------
# sns.scatterplot(x="total_bill", 
#                 y="tip",hue="sex",
#                 style="smoker",
#                 size="size",
#                 data=tips,palette="deep",
#                 #markers={"male":"D","female":"x"},
#                 )

# sns.regplot(x="size", 
#                 y="tip",data=tips,
#                 x_jitter=0.25, #change the botton design
#                 x_estimator=np.mean
#                 )