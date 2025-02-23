import os
import requests

#Define base URL for PokeAPI
base_url = "https://pokeapi.co/api/v2"
#Fnc to get pokemon types and evolution stage from PokeAPI
def get_pokemon_info(name):
    url = f"{base_url}/pokemon/{name.lower()}"
    response = requests.get(url)

    #200 is success
    if response.status_code == 200:
        data = response.json()

        #Getting types of the pokemons
        types = [t['type']['name'].capitalize() for t in data['types']]

        #Getting species data to get evolution chain URL
        species_url = data['species']['url']
        species_response = requests.get(species_url)
        species_data = species_response.json()

        #Getting Evo data
        evolution_chain_url = species_data['evolution_chain']['url']
        evolution_response = requests.get(evolution_chain_url)
        evolution_data = evolution_response.json()

        #Determine evolution stage, using 1 as default
        evolution_stage = 1  
        current_evo = evolution_data["chain"]

        #Looping and incrementing through evos for each of their stages
        while current_evo:
            if current_evo["species"]["name"] == name.lower():
                break
            evolution_stage += 1
            if current_evo["evolves_to"]:
                current_evo = current_evo["evolves_to"][0]
            else:
                break

        return types, evolution_stage
    else:
        print(f"Error for the data retrieval of {name}")
        return None, None


data_path = "ProcessedPokemonDataGen1"

#image counter
img_index = 1  

#Loop through all folders
#os.listdir(dataset_path) Gets list of all folder names using pokemon as var
for pokemon in os.listdir(data_path):
    pokemon_path = os.path.join(data_path, pokemon)

    #Check folder exists
    if os.path.isdir(pokemon_path):
        print(f"\n Renaming images for: {pokemon}")

        #Getting types and evolution stage from PokeAPI
        types, evolution_stage = get_pokemon_info(pokemon)

        if not types or evolution_stage is None:
            print(f"Skipping {pokemon}, data not found.")
            continue

        #Pokemons with no 2nd type will be defaulted to none
        type1 = types[0]
        type2 = types[1] if len(types) > 1 else "None"  


        #Loop through images and rename them
        for idx, image_name in enumerate(os.listdir(pokemon_path), start=1):
            if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):

                #Extract file extension
                file_extension = image_name.split('.')[-1]

                #New file name and img index
                new_name = f"{pokemon}_{type1}_{type2}_Stage{evolution_stage}_{img_index}.{file_extension}"


                #Full paths
                old_path = os.path.join(pokemon_path, image_name)
                new_path = os.path.join(pokemon_path, new_name)

                #Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {image_name} → {new_name}")

                img_index += 1  

print("\nRenamed done!")
