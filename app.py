import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import json

model_path = 'handwritten_character_recognition_model.h5'  
with open('class_labels.json', 'r') as f:
    class_labels = json.load(f)
    class_labels = {int(k): v for k, v in class_labels.items()}

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((28, 28))  
    img = img.convert('L') 
    img = np.array(img) / 255.0 
    img = np.expand_dims(img, axis=0)
    img = np.expand_dims(img, axis=-1)
    return img

def predict_character(image_path):
    model = tf.keras.models.load_model(model_path)
    img = preprocess_image(image_path)
    prediction = model.predict(img)
    predicted_class = np.argmax(prediction, axis=1)[0]
    character = class_labels[predicted_class]
    return character

def upload_image():
    file_path = filedialog.askopenfilename(title="Choose an Image")
    if file_path:
        img = Image.open(file_path)
        img = img.resize((200, 200))  # Resize image for display
        img = ImageTk.PhotoImage(img)
        panel.config(image=img)
        panel.image = img
        character = predict_character(file_path)
        result_label.config(text=f"Predicted Character: {character}")
        
root = tk.Tk()
root.title("Handwritten Character Recognition")
root.geometry("400x300")

panel = tk.Label(root)
panel.pack(pady=10)

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

result_label = tk.Label(root, text="Predicted Character:", font=('Times New Roman', 18, 'bold'))

result_label.pack(pady=20)

root.mainloop()
