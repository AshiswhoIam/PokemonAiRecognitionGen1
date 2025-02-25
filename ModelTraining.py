import tensorflow as tf
from tensorflow import keras
from keras import layers, models
normalization_layer = tf.keras.layers.Rescaling(1./255)

dataset_path = "SplitProcessedPokemonDataGen1"

#Load Training Data
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/train',
    image_size=(224, 224),
    batch_size=32,
    label_mode='int',
    shuffle=True
).map(lambda x, y: (normalization_layer(x), y))

#Load Validation Data
val_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/validation',
    image_size=(224, 224),
    batch_size=32,
    label_mode='int',
    shuffle=False
).map(lambda x, y: (normalization_layer(x), y))

#Load Test Data
test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/test',
    image_size=(224, 224),
    batch_size=32,
    label_mode='int',
    shuffle=False
).map(lambda x, y: (normalization_layer(x), y))

print(f"Train dataset: {train_dataset}")
print(f"Validation dataset: {val_dataset}")
print(f"Test dataset: {test_dataset}")

# Checking if images are normalized
image_batch, label_batch = next(iter(train_dataset))

# Check min and max pixel values after normalization
print("Min pixel value (after normalization):", tf.reduce_min(image_batch).numpy())
print("Max pixel value (after normalization):", tf.reduce_max(image_batch).numpy())



