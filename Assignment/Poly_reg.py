import matplotlib.pyplot as plt
import pandas as pd
from sklearn.linear_model import  LinearRegression
from sklearn.preprocessing import PolynomialFeatures

df = pd.read_csv('orders.csv')
print(df)

plt.scatter(df.days,df.amount)
poly = PolynomialFeatures(degree=4)
x_poly = poly.fit_transform(df[['days']])

reg = LinearRegression()
reg.fit(x_poly,df[['amount']])

plt.plot(df[['days']].values,reg.predict(poly.fit_transform(df[['days']])))
plt.show()



print(reg.predict(poly.fit_transform([[8]])))