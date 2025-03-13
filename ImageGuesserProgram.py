import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
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
        return {
            "Name": pokemon.capitalize(),
            "Types": types,
            "Height": f"{height} m",
            "Weight": f"{weight} kg",
            "Sprite": sprite_url
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

print(f"\nThe predicted Pokémon is: {predicted_pokemon}")
print(f"\n{predicted_pokemon} has the following attributes:")


#fetch info
pokemon_info = fetch_pokemon_info(predicted_pokemon)

img_display=Image.open(user_image_path).convert("RGB")

fig, ax = plt.subplots(figsize=(6, 6))
ax.imshow(img_display)
ax.axis("off")
ax.set_title(f"Predicted: {predicted_pokemon}", fontsize=14, fontweight="bold")

#Information display
if pokemon_info:
    info_text = f"Name: {pokemon_info['Name']}\n" \
                f"Types: {pokemon_info['Types']}\n" \
                f"Height: {pokemon_info['Height']}\n" \
                f"Weight: {pokemon_info['Weight']}"

    #Draw the info on the image
    draw = ImageDraw.Draw(img_display)
    try:
        font = ImageFont.truetype("arial.ttf", 16)
    except IOError:
        font = ImageFont.load_default()

    text_position = (10, 10)
    text_color = (255, 255, 255) 

    #Text pred display
    text_bg_position = (5, 5, 230, 80)
    draw.rectangle(text_bg_position, fill=(0, 0, 0, 180))
    draw.text(text_position, info_text, fill=text_color, font=font)

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



