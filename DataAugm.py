import os
import shutil
import random
import numpy as np
from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt

dataset_path = 'PokemonDataGen1' 
augmented_folder_path = 'MoreAugProcessedGen1Pokemons' 

#Create folder if it doesn't exist
if not os.path.exists(augmented_folder_path):
    os.makedirs(augmented_folder_path)

#function to apply random augmentation
def augment_image_OG(image):
    #Convert image to RGB 
    if image.mode == 'RGBA' or image.mode == 'P':
        image = image.convert('RGBA')
    
    elif image.mode != 'RGB':
        image = image.convert('RGB')

    #Guaranteed Horizontal flip
    image = image.transpose(Image.FLIP_LEFT_RIGHT)
    
    #Extreme Brightness
    enhancer = ImageEnhance.Brightness(image)
    brightness_factor = random.choice([0.6, 1.4])
    image = enhancer.enhance(brightness_factor)

    #Random rotation between -30 and +30 degrees
    angle = random.randint(-30, 30)
    image = image.rotate(angle)

    return image

def augment_image_New(image):

    if image.mode == 'RGBA' or image.mode == 'P':
        image = image.convert('RGBA')
    
    elif image.mode != 'RGB':
        image = image.convert('RGB')

    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(random.choice([0.7, 1.3]))

    image = image.rotate(random.randint(-35, 35))

    enhancer = ImageEnhance.Color(image)
    image = enhancer.enhance(random.uniform(0.8, 1.2))

    return image

#Copy the original images to the new folder
def copy_original_images():
    for class_name in os.listdir(dataset_path):
        class_folder = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_folder):
            #Create corresponding class folder in the augmented folder
            new_class_folder = os.path.join(augmented_folder_path, class_name)
            if not os.path.exists(new_class_folder):
                os.makedirs(new_class_folder)

            #Copy original images to the new folder
            for image_name in os.listdir(class_folder):
                src_image_path = os.path.join(class_folder, image_name)
                dst_image_path = os.path.join(new_class_folder, image_name)
                shutil.copy(src_image_path, dst_image_path)

#Function to save augmented images
def save_augmented_image(image, idx, class_name,aug_og_new):
    # Ensure the class folder exists
    class_folder = os.path.join(augmented_folder_path, class_name)
    if not os.path.exists(class_folder):
        os.makedirs(class_folder)
    
    #Convert image to RGB if it's in RGBA mode
    if image.mode == 'RGBA':
        image = image.convert('RGB')

    #Save the augmented image
    image_filename = f"{class_name}_augmented_{idx}_{aug_og_new}.jpg"
    image_path = os.path.join(class_folder, image_filename)
    
    #Save the image using PIL's save method
    image.save(image_path)

#Apply augmentation and save the augmented images
def apply_augmentation_and_save():
    copy_original_images()

    #Iterate through the dataset, apply augmentation, save augmented images
    class_idx = 0
    for class_name in os.listdir(dataset_path):
        class_folder = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_folder):
            for idx, image_name in enumerate(os.listdir(class_folder)):
                image_path = os.path.join(class_folder, image_name)
                
                #Open image using Pillow
                image = Image.open(image_path)

                #Apply augmentation
                augmented_image_OG = augment_image_OG(image)
                #Save augmented image with class name and index
                save_augmented_image(augmented_image_OG, idx, class_name,1)

                augmented_image_New = augment_image_New(image)
                #Save augmented image with class name and index
                save_augmented_image(augmented_image_New, idx, class_name,2)

                if (idx + 1) % 100 == 0:
                    print(f"Processed {idx + 1} images in class {class_name}")
    
    print(f"Original and augmented images saved to: {augmented_folder_path}")

apply_augmentation_and_save()
