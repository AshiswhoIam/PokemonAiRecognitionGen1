import os

data_path = "PokemonDataGen1"

#image counter
img_index = 1  

#Loop through all folders
#os.listdir(dataset_path) Gets list of all folder names using pokemon as var
for pokemon in os.listdir(data_path):
    pokemon_path = os.path.join(data_path, pokemon)

    #Check folder exists
    if os.path.isdir(pokemon_path):
        print(f"\n Renaming images for: {pokemon}")

        #Loop through images and rename them
        for idx, image_name in enumerate(os.listdir(pokemon_path), start=1):
            if image_name.lower().endswith(('.jpg', '.jpeg', '.png')):

                #Extract file extension
                file_extension = image_name.split('.')[-1]

                #New file name and img index
                new_name = f"{pokemon}_{img_index}.{file_extension}"

                #Full paths
                old_path = os.path.join(pokemon_path, image_name)
                new_path = os.path.join(pokemon_path, new_name)

                #Rename the file
                os.rename(old_path, new_path)
                print(f"Renamed: {image_name} → {new_name}")

                img_index += 1  

print("\nRenamed done!")
