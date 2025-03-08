import matplotlib.pyplot as plt
import os

def plot_class_distribution(dataset_path):
    #list of class names
    class_names = os.listdir(dataset_path)
    class_counts = []

    #Loop through each class folder and count the number of images
    for class_name in class_names:
        class_path = os.path.join(dataset_path, class_name)
        if os.path.isdir(class_path):
            count = len(os.listdir(class_path))
            class_counts.append(count)

    #Create plot
    plt.figure(figsize=(12, 8))
    plt.barh(class_names, class_counts, color='turquoise')
    plt.xlabel('Number of Images')
    plt.ylabel('Pokemons')
    plt.title('Class Distribution in Dataset')
    plt.tight_layout()


    plt.show()


dataset_path = 'PokemonDataGen1Augmented' 
plot_class_distribution(dataset_path)
