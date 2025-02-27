import time
import tensorflow as tf
from tensorflow.keras import layers, models 
from tensorflow.keras import mixed_precision
import matplotlib.pyplot as plt
from tensorflow.keras.callbacks import EarlyStopping
from tensorflow.keras import regularizers
mixed_precision.set_global_policy('mixed_float16')

physical_devices = tf.config.list_physical_devices('GPU')
if physical_devices:
    for device in physical_devices:
        tf.config.experimental.set_memory_growth(device, True)
    
    gpu_details = tf.config.experimental.get_device_details(physical_devices[0])
    print("GPU detected:", physical_devices[0])
    print("GPU details:", gpu_details)
     #Logging device
    tf.debugging.set_log_device_placement(True)
else:
    print("No GPU found CPU will be used.")

# Manually normalize the images by dividing by 255
def normalize_image(image, label): 
    return image / 255.0, label


dataset_path = "SplitProcessedPokemonDataGen1"

#Load Training Data
train_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/train',
    image_size=(224, 224),
    batch_size=64,
    label_mode='int',
    shuffle=True
).map(normalize_image)

#Load Validation Data
validation_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/validation',
    image_size=(224, 224),
    batch_size=64,
    label_mode='int',
    shuffle=False
).map(normalize_image)

#Load Test Data
test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/test',
    image_size=(224, 224),
    batch_size=64,
    label_mode='int',
    shuffle=False
).map(normalize_image)

print(f"Train dataset: {train_dataset}")
print(f"Validation dataset: {validation_dataset}")
print(f"Test dataset: {test_dataset}")

# Checking if images are normalized
image_batch, label_batch = next(iter(train_dataset))

# Check min and max pixel values after normalization
print("Min pixel value (after normalization):", tf.reduce_min(image_batch).numpy())
print("Max pixel value (after normalization):", tf.reduce_max(image_batch).numpy())
print("Waiting for 5 seconds before starting training...")
time.sleep(5)

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

    layers.Conv2D(512, (3, 3), activation='relu'),
    layers.MaxPooling2D(2, 2),
    layers.BatchNormalization(),
    
    #Fully con layers
    layers.Flatten(),
    layers.Dense(512, activation='relu', kernel_regularizer=regularizers.l2(0.01)),
    # Prevents overfitting
    layers.Dropout(0.5),  
    #151 classes
    layers.Dense(151, activation='softmax')
])

#Compile the model start with smaller learning rate for stability
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.0001),
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

#stopping early to prevent overfitting
early_stopping = EarlyStopping(monitor='val_loss', patience=3, restore_best_weights=True)

#Train the model
history = model.fit(
    train_dataset,
    epochs=20,
    verbose=1,
    validation_data=validation_dataset,
    callbacks=[early_stopping]

)
plt.plot(history.history['loss'], label='Train Loss')
plt.plot(history.history['val_loss'], label='Val Loss')
plt.xlabel('Epoch')
plt.ylabel('Loss')
plt.legend()
plt.title('Training vs Validation Loss')
plt.show()
#Model Accuracy
test_loss, test_accuracy = model.evaluate(test_dataset)
print(f"Test accuracy: {test_accuracy*100:.2f}%")
print(f"Test Loss: {test_loss:.4f}")

#Save model
model.save('Dexter_pokemon_model1.h5')