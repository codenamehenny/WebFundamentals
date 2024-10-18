#1. Exploring Web Technologies and Python Programming

# Fetching Data from the Pokémon API
# 1. Write a Python script to make a GET request to the Pokémon API (`https://pokeapi.co/api/v2/pokemon/pikachu`).
# 2. Extract and print the name and abilities of the Pokémon.

# fetching data from the Pokemon API
import requests
import json

pikachu_response = requests.get('https://pokeapi.co/api/v2/pokemon/pikachu')
pikachu_json = pikachu_response.text

# parsing JSON response
pikachu_data = json.loads(pikachu_json)
pikachu = pikachu_data['name'].title()
pikachu_abilities = [ability['ability']['name'] for ability in pikachu_data['abilities']]
print(f"Name: {pikachu} --- Abilities: {', '.join(pikachu_abilities)} ")

# Analyzing and Displaying Data
#1. Modify the script to fetch data for three different Pokémon.
#2. Create a function to calculate and return the average weight of these Pokémon.
#3. Print the names, abilities, and average weight of the three Pokémon.

# fetches pokemon data by its name
def fetch_pokemon_data(pokemon_name):
    try:
        url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
        response = requests.get(url)
        json_data = response.text
        data = json.loads(json_data)
        # extracting relevant info and placing in dictionary
        pokemon_info = {
            'name': data['name'],
            'abilities': [ability['ability']['name'] for ability in data['abilities']],
            'weight': data['weight']
        }
        return pokemon_info if pokemon_info else None    
    except Exception as e:
        print(f"Error Message: {e}. Please try again")

# calculating the average weight of the pokemon list
def calculate_average_weight(pokemon_list):
    total_weight = sum(pokemon['weight'] for pokemon in pokemon_list)
    return total_weight / len(pokemon_list)

pokemon_names = ["pikachu", "bulbasaur", "charmander"]

# fetching data for each pokemon
pokemon_data_list = [fetch_pokemon_data(name) for name in pokemon_names]

if pokemon_data_list:
    try:
        average_weight = calculate_average_weight(pokemon_data_list)
        # organizes Pokémon details
        print("\n
        Here's each Pokémon's data:\n")
        for pokemon in pokemon_data_list:
            print(f"Name: {pokemon['name'].title()}")
            print(f"Abilities: {', '.join(pokemon['abilities'])}")
            print(f"Weight: {pokemon['weight']}\n")
        print(f"Average Pokémon weight is roughly {average_weight:.0f}")
    except Exception as e:
        print(f"Error Message: {e}. Please try again")   
else:
    print("Whoops, Pokémon list empty.")