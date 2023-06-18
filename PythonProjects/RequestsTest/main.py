import requests
import json

token = '6c2e858919748c6430a2ce5585400e05'
host = 'https://pokemonbattle.me:9104'


сreation = requests.post(f'{host}/pokemons', json =
                         {
    "name": "Бамблби",
    "photo": "https://dolnikov.ru/pokemons/albums/191.png"
                         }, headers = {"trainer_token" : token, "Content-Type" : "application/json"})

print(сreation.text)


name_change = requests.put(f'{host}/pokemons', json =
                         {
    "pokemon_id": "12906",
    "name": "Бам",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
                         }, headers = {"trainer_token" : token, "Content-Type" : "application/json"})

print(name_change.text)

add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json =
                         {
    "pokemon_id": "12906",
                         }, headers = {"trainer_token" : token, "Content-Type" : "application/json"})


print(add_pokeball.text)


                               