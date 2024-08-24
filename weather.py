import requests

api="3a0b617dac50165aac6ffff7f7d6951d"
city=input("enter city     :")
url=f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api}&units=metric"

response=requests.get(url)
x=response.json()

if response.status_code==200:
    humidity=x["main"]["humidity"]
    pressure=x["main"]["pressure"]
    wind=x["wind"]["speed"]
    descrpition=x["weather"][0]["description"]
    temp=x["main"]["temp"]

    print("humidity    :",humidity)
    print("pressure     :",pressure)
    print("wind     :",wind)
    print("descrpition     :",descrpition)
    print("temp     :",temp)

else:
    print("error:",x.get("message","unable to fetch weather data"))