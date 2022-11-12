import pandas as pd
from sklearn import linear_model

df = pd.read_csv("orders.csv")
# print(df)
reg = linear_model.LinearRegression()
reg.fit(df[['user', 'orders', 'age ']],df.amount)
print(reg.predict([[6000,22000,22]]))
