import tensorflow as tf
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt

# Load model
model = tf.keras.models.load_model('Dexter_PokemonGen1Ai27.h5')

dataset_path = "SplitTryThisSetPokemonGen1"
test_dataset = tf.keras.preprocessing.image_dataset_from_directory(
    dataset_path + '/test',
    image_size=(224, 224),
    batch_size=64,
    label_mode='int',
    shuffle=False
)
#Get true labels and predictions
y_true = []
y_pred = []
for images, labels in test_dataset:
    y_true.extend(labels.numpy())  
    predictions = model.predict(images)
    y_pred.extend(np.argmax(predictions, axis=1))

#Save classification report
report = classification_report(y_true, y_pred, target_names=test_dataset.class_names, digits=4)
with open("classification_report.txt", "w") as f:
    f.write(report)

#Plot confusion matrix
conf_matrix = confusion_matrix(y_true, y_pred)
fig, ax = plt.subplots(figsize=(15, 12))
ax.matshow(conf_matrix, cmap="Blues")
for i in range(conf_matrix.shape[0]):
    for j in range(conf_matrix.shape[1]):
        ax.text(j, i, str(conf_matrix[i, j]), ha='center', va='center', color='black', fontsize=6)

plt.xlabel("Predicted Label")
plt.ylabel("True Label")
plt.title("Confusion Matrix")
plt.xticks(ticks=np.arange(len(test_dataset.class_names)), labels=test_dataset.class_names, rotation=90, fontsize=6)
plt.yticks(ticks=np.arange(len(test_dataset.class_names)), labels=test_dataset.class_names, fontsize=6)
plt.savefig("confusion_matrix27.png")
plt.show()
