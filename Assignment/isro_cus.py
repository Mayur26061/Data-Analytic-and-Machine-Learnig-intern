import requests
from matplotlib import pyplot as plt
url1=requests.get("https://isro.vercel.app/api/spacecrafts")
url2=requests.get("https://isro.vercel.app/api/customer_satellites")
isr=url1.json()
cus=url2.json()
lst=list()
lst.append(len(isr["spacecrafts"]))
lst.append(len(cus["customer_satellites"]))
plt.pie(lst,labels=["ISRO Own Satellites","Customer Satellites"],autopct='%1.0f%%')
plt.show()