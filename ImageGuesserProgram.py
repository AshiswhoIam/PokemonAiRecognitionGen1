import os
import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
import tkinter as tk
from tkinter import filedialog

#root = tk.Tk()
#root.withdraw()

model_path= ""
model=tf.keras.models.load_model(model_path)

#retrieve class names
test_image_folder = 'SplitProcessedPokemonDataGen1/test'
pokemon_classes=sorted(os.listdir(test_image_folder))

def reform_image(path,size=(224,224)):
    image=Image.open(path).convert("RGB")
    image=image.resize(size)
    image_arr=np.array(image)/255.0
    image_arr=np.expand_dims(image_arr,axis=0)
    return image_arr

img_reformed=reform_image("some path here")

#Do the prediction save idx to map to the pokemon
prediction=model.predict(img_reformed)
predict_idx=np.argmax(prediction,axis=1)[0]
predited_pokemon=pokemon_classes[predict_idx]

img_display=Image.open("some path here").convert("RGB")

draw = ImageDraw.Draw(img_display)
try:
    font = ImageFont.truetype("arial.ttf", 20)
except IOError:
    font = ImageFont.load_default()

text = f"Predicted: {predited_pokemon}"
text_position = (10, 10)

