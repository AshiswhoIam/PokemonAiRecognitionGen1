import os
import shutil
import random

#processed imgs
dataset_path = "TryThisSetPokemonGen1"

#splitted folders
splitData_folder = "SplitTryThisSetPokemonGen1"

train_ratio = 0.8  
val_ratio = 0.1    
test_ratio = 0.1

#check if existing train val test
for split in ["train", "validation", "test"]:
    split_path = os.path.join(splitData_folder, split)
    os.makedirs(split_path, exist_ok=True)

# Loop through all folders
#os.listdir(dataset_path) Gets list of all folder names using pokemon as var
for pokemon in os.listdir(dataset_path):
    pokemon_path = os.path.join(dataset_path, pokemon)

    if os.path.isdir(pokemon_path):
        #randomize img selection
        images = os.listdir(pokemon_path)
        random.shuffle(images)

        #Calculate split indices
        total_images = len(images)
        train_idx = int(total_images * train_ratio)
        validation_idx = train_idx + int(total_images * val_ratio)

        #Creating folders
        for split in ["train", "validation", "test"]:
            os.makedirs(os.path.join(splitData_folder, split, pokemon), exist_ok=True)

        #splitting iamges to each folder
        for i, img_name in enumerate(images):
            #full path
            src_path = os.path.join(pokemon_path, img_name)

            if i < train_idx:
                dest_path = os.path.join(splitData_folder, "train", pokemon, img_name)
            elif i < validation_idx:
                dest_path = os.path.join(splitData_folder, "validation", pokemon, img_name)
            else:
                dest_path = os.path.join(splitData_folder, "test", pokemon, img_name)

            shutil.move(src_path, dest_path)

print("Dataset split done hopefully.")
