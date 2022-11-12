import requests
import pandas as pd
from sklearn import linear_model
url = requests.get("https://data.covid19india.org/data.json")
data = url.json()
df = pd.DataFrame(data['cases_time_series'])
reg = linear_model.LinearRegression()
reg.fit(df[['totalconfirmed']],df[['totaldeceased']])
print(reg.predict([[32520545]]))