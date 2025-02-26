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


#------------------------------------------------------------------------------------
#CNN Model
model = tf.keras.Sequential([
    #64 because larger data set 3x3 kernel
    layers.Conv2D(64, (3, 3), activation='relu', input_shape=(224, 224, 3)),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),
    
    layers.Conv2D(128, (3, 3), activation='relu'),
    layers.BatchNormalization(),
    layers.MaxPooling2D(2, 2),
    
    layers.Conv2D(256, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    
    #Fully con layers
    layers.Flatten(),
    layers.Dense(256, activation='relu'),
    layers.Dropout(0.5),  # Prevents overfitting
    #151 classes
    layers.Dense(151, activation='softmax')
])

#Compile the model start with smaller learning rate for stability
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0005),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#Train the model
history = model.fit(
    train_dataset,
    epochs=20,
    validation_data=val_dataset
)

#Model Accuracy
test_loss, test_accuracy = model.evaluate(test_dataset)
print(f"Test accuracy: {test_accuracy*100:.2f}%")

#Save model
model.save('Dexter_pokemon_model1.h5')