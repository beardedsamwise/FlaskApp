from flask import Flask
import requests
import random

app = Flask(__name__)


@app.route("/")
def index():
    pokemon = random_pokemon()
    return("<h1>RANDOM POKEMON GENERATOR</h1>"
           "Random Pokemon: " + pokemon)


def random_pokemon():
    int = random.randint(1, 150)
    base_url = "https://pokeapi.co/api/v2/pokemon/"
    random_url = base_url + str(int)
    response = requests.get(random_url)
    json = response.json()
    pokemon = json.get('name')
    return pokemon


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
