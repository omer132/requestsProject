import requests

url="https://hacker-news.firebaseio.com/v0/topstories.json"
resception=requests.get(url)
x=resception.json()
y=x[:30]

for i in y:
    urlll=f"https://hacker-news.firebaseio.com/v0/item/{i}.json"
    v=requests.get(urlll)
    b=v.json()

    title=b.get("title","No title")
    ur=b.get("Url","No URL")
    score=b.get("score","No score")

    print(f"title:{title}")
    print(f"url:{ur}")
    print(f"score:{score}")
    print("-"*40)