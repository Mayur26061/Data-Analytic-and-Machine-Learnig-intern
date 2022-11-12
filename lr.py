import matplotlib.pyplot as plt
from sklearn import linear_model
import pandas as pd
data=pd.read_csv("Area.csv")
print(data)
plt.xlabel('area')
plt.ylabel('prices')
plt.scatter(data.area,data.price,color="red")
plt.show()
reg=linear_model.LinearRegression()
reg.fit(data[['area']],data[['price']])
print(reg.predict([[3300]]))
#y=bo+b1x
print(reg.coef_) #b1
print(reg.intercept_)#b0
print(reg.intercept_+reg.coef_*3300)