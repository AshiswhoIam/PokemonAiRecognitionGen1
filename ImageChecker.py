import os

data_path = "PokemonDataGen1"  

#Array storage for folders that need fixing
missing_img_folders = []
#Storage for gifs to check which folders
gif_folders = []

#Variables to count each type of files
jpg_count = 0
jpeg_count = 0
png_count = 0

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

        #print(f"{pokemon}: {image_count} images all good check check" if image_count == 100 else f"{pokemon}: {image_count} images not to folder XXXXXX")

        # Check for GIF files specifically
        gif_files = [f for f in os.listdir(pokemon_path) if f.lower().endswith('.gif')]
        # Append folders containing GIFs
        if gif_files:
            gif_folders.append((pokemon, len(gif_files)))

        #JPG, JPEG, and PNG images
        jpg_count += len([f for f in os.listdir(pokemon_path) if f.lower().endswith('.jpg')])
        jpeg_count += len([f for f in os.listdir(pokemon_path) if f.lower().endswith('.jpeg')])
        png_count += len([f for f in os.listdir(pokemon_path) if f.lower().endswith('.png')])


if missing_img_folders:
    print("\nThe following pokemon folders don't have 100 images:")
    for folder, count in missing_img_folders:
        print(f"- {folder}: {count} images")
else:
    print("\nAll the folders have 100imgs")


if gif_folders != []:
    print("\nThe following folders have gifs:")
    for folder, count in gif_folders:
        print(f"- {folder}: {count} gifs")
else:
    print("\nThe data has no gifs.")

#Total images and each file type
print("\nTotal images types and total dataset:")
print(f"- JPG images: {jpg_count}")
print(f"- JPEG images: {jpeg_count}")
print(f"- PNG images: {png_count}")
print(f"- Total images: {jpg_count+jpeg_count+png_count}")