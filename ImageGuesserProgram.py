import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image
import tkinter as tk
from tkinter import filedialog
import requests

root = tk.Tk()
root.withdraw()

user_image_path = filedialog.askopenfilename(
    title="Choose a pokemon image file to get predicted:",
    filetypes=[("Image files", "*.jpg *.jpeg *.png")]
)

if not user_image_path:
    print("No file selected. Exiting.")
    exit()


model_path= "Dexter_PokemonGen1Ai27.h5"
model=tf.keras.models.load_model(model_path)

#retrieve class names
test_image_folder = 'SplitProcessedPokemonDataGen1/test'
pokemon_classes=sorted(os.listdir(test_image_folder))

#this method to fetch info from api
def fetch_pokemon_info(pokemon):
    url =  f"https://pokeapi.co/api/v2/pokemon/{pokemon.lower()}"
    response = requests.get(url)

    if response.status_code ==200:
        data = response.json()
        types = ", ".join([t['type']['name'].capitalize() for t in data['types']])
        height = data['height'] / 10 
        weight = data['weight'] / 10 
        sprite_url = data['sprites']['front_default'] 
        species_url = data['species']['url']
        species_response = requests.get(species_url)
        #Fetch Habitat info
        habitat = "Unknown"
        if species_response.status_code == 200:
            species_data = species_response.json()
            if 'habitat' in species_data and species_data['habitat']:
                habitat = species_data['habitat']['name'].capitalize()
            
        #Fetch Flavour Text aka Pokédex Description
            for entry in species_data['flavor_text_entries']:
                if entry['language']['name'] == 'en':
                    flavor_text = entry['flavor_text']
                    break

        flavor_text = flavor_text.replace("\n", " ")
        flavor_text = ' '.join(flavor_text.split())
        return {
            "Name": pokemon.capitalize(),
            "Types": types,
            "Height": f"{height} m",
            "Weight": f"{weight} kg",
            "Sprite": sprite_url,
            "Habitat": habitat,
            "Flavour Text": flavor_text
        }
    
    else:
        return None

#just pre process image given
def reform_image(path,size=(224,224)):
    image=Image.open(path).convert("RGB")
    image=image.resize(size)
    image_arr=np.array(image)/255.0
    image_arr=np.expand_dims(image_arr,axis=0)
    return image_arr

img_reformed=reform_image(user_image_path)

#Do the prediction save idx to map to the pokemon
prediction=model.predict(img_reformed)
predict_idx=np.argmax(prediction,axis=1)[0]
predicted_pokemon=pokemon_classes[predict_idx]
#fetch info
pokemon_info = fetch_pokemon_info(predicted_pokemon)

print(f"\nThe predicted Pokémon is: {predicted_pokemon}")
print(f"\n{predicted_pokemon} has the following attributes:\n"
      f"Name: {pokemon_info['Name']}\n"
      f"Types: {pokemon_info['Types']}\n"
      f"Height: {pokemon_info['Height']}\n"
      f"Weight: {pokemon_info['Weight']}\n"
      f"Habitat: {pokemon_info['Habitat']}\n"
      f"Flavour Text: {pokemon_info['Flavour Text']}")


img_display=Image.open(user_image_path).convert("RGB")

#Information display
if pokemon_info:
    #Sprite display 
    sprite_url = pokemon_info.get("Sprite")
    if sprite_url:
        sprite_img = Image.open(requests.get(sprite_url, stream=True).raw)
        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
        ax1.imshow(img_display)
        ax1.axis("off")
        ax1.set_title(f"Predicted: {predicted_pokemon}", fontsize=14, fontweight="bold")

        ax2.imshow(sprite_img)
        ax2.axis("off")
        ax2.set_title(f"{predicted_pokemon} Sprite", fontsize=14)

plt.tight_layout()
plt.show()



