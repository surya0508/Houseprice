import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import pickle

dataset=pd.read_csv('D:\spyderf\homeprices.csv')
dataset.head()

#**Data Preprocessing: Fill NA values with median value of a column
dataset.bedrooms.median()
dataset.bedrooms = dataset.bedrooms.fillna(dataset.bedrooms.median())
dataset
from sklearn import linear_model
reg = linear_model.LinearRegression()
reg.fit(dataset.drop('price',axis='columns'),dataset.price)

#saving model to disk

pickle.dump(reg, open('model.pkl','wb'))

#loading model to compare results

model=pickle.load(open('model.pkl','rb'))
print(model.predict([[3000,3,40]]))
