import requests
import matplotlib.pyplot as plt
url=requests.get("http://universities.hipolabs.com/search?country=United+Kingdom")
uk=url.json()
url1=requests.get("http://universities.hipolabs.com/search?country=United+States")
us=url1.json()
url2=requests.get("http://universities.hipolabs.com/search?country=india")
ind=url2.json()
url3=requests.get("http://universities.hipolabs.com/search?country=pakistan")
pak=url3.json()
countries = ['United Kingdom', 'United States', 'India', 'Pakistan']
totaluniversities = [len(uk), len(us), len(ind), len(pak)]

# fig = plt.figure(figsize=(15,10))
plt.bar(countries, totaluniversities)
plt.xlabel("COUNTRIES")
plt.ylabel("TOTAL UNIVERSITIES")
plt.show()
# search mechanism
inuputcountry = input('Enter Country Name: ')
inuputuniversity = input('Enter University Name: ')
n = 0
data = []
if inuputcountry.lower() == 'india':
    n = len(ind)
    data = ind
elif inuputcountry.lower() == 'united kingdom':
    n = len(uk)
    data = uk
elif inuputcountry.lower() == 'united states':
    n = len(us)
    data = us
elif inuputcountry.lower() == 'pakistan':
    n = len(pak)
    data = pak
else:
    print('Please enter a valid country name')
    exit()

for i in range(0,n):
    if inuputcountry.lower() == data[i]['country'].lower() and inuputuniversity.lower() == data[i]['name'].lower():
        print('University Found', ' Visit - ', data[i]['web_pages'])
        exit()
else:
    print('University Not Found')