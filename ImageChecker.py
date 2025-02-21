import os

data_path = "PokemonDataGen1"  

#Array storage for folders that need fixing
missing_img_folders = []

# Loop through all folders
#os.listdir(dataset_path) Gets list of all folder names using pokemon as var
for pokemon in os.listdir(data_path):
    #creating full path using.join
    pokemon_path = os.path.join(data_path, pokemon)

    #Check folder exists
    if os.path.isdir(pokemon_path):
        # Count all images
        image_count = len([f for f in os.listdir(pokemon_path) if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))])

        #append stores as tuples
        if image_count != 100:
            missing_img_folders.append((pokemon, image_count))

        print(f"{pokemon}: {image_count} images all good check check" if image_count == 100 else f"{pokemon}: {image_count} images not to folder XXXXXX")


if missing_img_folders:
    print("\nThe following pokemon folders don't have 100 images:")
    for folder, count in missing_img_folders:
        print(f"- {folder}: {count} images")
else:
    print("\nAll the folders have 100imgs")
