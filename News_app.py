import requests
import json

query=input("News about: ")
url=f"https://newsapi.org/v2/everything?q={query}&from=2023-08-08&sortBy=publishedAt&apiKey=0d2dd7ca58d645a7a3fb0215317a4ebe"

r=requests.get(url)
news=json.loads(r.text)

for i in news["articles"]:
    print(i["title"])
    print(i["description"])
    print("-----------------------------------------------------------")
    print("-----------------------------------------------------------")
    
