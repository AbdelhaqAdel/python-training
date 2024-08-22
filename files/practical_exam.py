# import numpy as np
import pandas as pd
# import matplotlib.pyplot as plt
# import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
# from sklearn import metrics


# import Data set ........
insurance_dataset = pd.read_csv('insurance.csv');

# show Data set ..........
insurance_dataset.head();


# checking for missing values
print(insurance_dataset.isnull().sum())
z=insurance_dataset.describe()

#Encoding the categorical feature.......

# encoding sex column
insurance_dataset.replace({'sex':{'male':0,'female':1}}, inplace=True)

 # encoding 'smoker' column
insurance_dataset.replace({'smoker':{'yes':0,'no':1}}, inplace=True)

# encoding 'region' column
insurance_dataset.replace({'region':{'southeast':0,'southwest':1,'northeast':2,'northwest':3}}, inplace=True)

#Splitting the Features and Target....

X = insurance_dataset.drop(columns='charges', axis=1)
Y = insurance_dataset['charges']



#Splitting the data into Training data & Testing Data.....

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)

#Linear Regression

regressor = LinearRegression()
regressor.fit(X_train, Y_train)


