import requests

pokemonName=input("enter pokemon name:  ")

url=f"https://pokeapi.co/api/v2/pokemon/{pokemonName}"
x=requests.get(url)

if x.status_code==200:
    y=x.json()
    
    name=y["name"].capitalize()
    weight=y["weight"]
    height=y["height"]
    base_experience=y["base_experience"]

    types=[typeee["type"]["name"]for typeee in y["types"]]
    abilities=[ability["ability"]["name"]for ability in y["abilities"]]
    stats={stat["stat"]["name"]  :stat["base_stat"]  for stat in y["stats"]}

    print(f"name:   {name}")
    print(f"weight: {weight} hectograms")
    print(f"height: {height} decimetres")
    print(f"base experience: {base_experience}")
    print(f"type: {" ,   ".join(types)}")
    print(f"abilities: {" ,    ".join(abilities)}")
    print("Stats:")
    
    for stat_name, stat_value in stats.items():
        print(f"    {stat_name.capitalize()}: {stat_value}")

