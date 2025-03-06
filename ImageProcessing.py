import os
import cv2
import numpy as np

#orignal data
og_folder = "PokemonDataGen1Augmented"
processed_folder = "ProcessedPokemonDataGen1"

#Creating folder if not exisiting yet
if not os.path.exists(processed_folder):
    os.makedirs(processed_folder)

#Loop through all folders
#os.listdir(dataset_path) Gets list of all folder names using pokemon as var
for pokemon in os.listdir(og_folder):
    pokemon_path = os.path.join(og_folder, pokemon)

    #Checking if folder directory
    if os.path.isdir(pokemon_path):
        print(f"Processing images for: {pokemon}")

        #joining paths
        processed_pokemon_path = os.path.join(processed_folder, pokemon)
        #creating each pokemon folder if not existing
        if not os.path.exists(processed_pokemon_path):
            os.makedirs(processed_pokemon_path)

        #Loop through images in the pokemon's folder
        for img_name in os.listdir(pokemon_path):
            if img_name.lower().endswith(('.jpg', '.jpeg', '.png')):  
                img_path = os.path.join(pokemon_path, img_name)

                # Read the image
                image = cv2.imread(img_path)
                if image is None:
                    print(f"Skipping {img_name} was not able to read this specific image")
                    continue

                #Convert BGR to RGB
                image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

                #Resize to 224x224
                image = cv2.resize(image, (224, 224))

                #Pixel Normalization
                image = image / 255.0  

                #Convert to 8-bit (back to 0-255 for saving)
                image = (image * 255).astype(np.uint8)

                #Save as PNG
                new_img_name = os.path.splitext(img_name)[0] + ".png"
                new_img_path = os.path.join(processed_pokemon_path, new_img_name)
                cv2.imwrite(new_img_path, image)

        print(f"Finished processing {pokemon}")

print("\nPreprocessing finished Images saved in:", processed_folder)
