import tensorflow as tf

# Define dataset path
dataset_path = "SplitProcessedPokemonDataGen1"

#Load Training Data
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/train',
    batch_size=32,
    label_mode='int',
    shuffle=True
)

#Load Validation Data
val_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/validation',
    image_size=(224, 224),
    batch_size=32,
    label_mode='int',
    shuffle=False
)

#Load Test Data
test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/test',
    batch_size=32,
    label_mode='int',
    shuffle=False
)

print(f"Train dataset: {train_dataset}")
print(f"Validation dataset: {val_dataset}")
print(f"Test dataset: {test_dataset}")
