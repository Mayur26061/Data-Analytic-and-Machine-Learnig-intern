import requests
url=requests.get("https://isro.vercel.app/api/spacecrafts")
data=url.json()
print("Total number of Main keys are-",len(data))
for i in data:
    print(i)
print("total number of space craft data :",len(data["spacecrafts"]))
for i in range(0,len(data["spacecrafts"])):
    print(data["spacecrafts"][i]["id"],":",data["spacecrafts"][i]["name"])
name=input("enter name of spacecraft")
for i in range(0,len(data["spacecrafts"])):
    if name==data["spacecrafts"][i]["name"]:
        print("spacecraft found")
        break
else:
    print("spacecraft not found")