"https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png"

import requests
import shutill
import json

class LLamadap3:

    def cosa_cosa(self):
        r = requests.get(url="https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/back/132.png")
        print(r.content)
        print(r.status_code)

    def nonono(self, url, file_name):
        res = requests.get(url,stream=True)

        if 200 == res.status_code:
            with open(file_name, "wb") as f:
                shutill.copyfileobj(res,raw,f)
            print("imagen descargs completamente")
        else:
            print("No se encontro nada")

    def cosa_cosa(self,pokemon):
        r = requests.get(url="https://pokeapi.co/api/v2/pokemon/"+pokemon)
        obj = json.loads(r.content)
        return obj["sprites"]["front_shiny"]
    
pokemon = input("Escoje un pokemon")
yoyo = LLamadap3()
ing = yoyo.cosas.cosa(pokemon)
yoyo.nonono(ing, str(pokemon)+".png")

