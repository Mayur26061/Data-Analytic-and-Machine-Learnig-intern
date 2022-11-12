import requests
url=requests.get("https://inshortsapi.vercel.app/news?category=sports")
data = url.json()

print("Number of main key", len(data))
print("All keys in API")
for i in data:
    print(i, end=" ")
for i in data["data"][0]:
    print(i, end=" ")
print()
print("There are total ", len(data["data"]), "news available")
print("all news in format")
for i in range(0, len(data["data"])):
    print(i+1, data["data"][i]["content"], ", AUTHOR:",data["data"][i]["author"], ", DATE:", data["data"][i]["date"])
