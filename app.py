import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import tensorflow as tf
import json

# Load the model and class labels
model_path = 'handwritten_character_recognition_model.h5'  # Model file
with open('class_labels.json', 'r') as f:
    class_labels = json.load(f)
    class_labels = {int(k): v for k, v in class_labels.items()}

def preprocess_image(image_path):
    img = Image.open(image_path)
    img = img.resize((28, 28))  # Resize image as per model input size
    img = img.convert('L')  # Convert to grayscale
    img = np.array(img) / 255.0  # Normalize
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

# Create the main GUI window
root = tk.Tk()
root.title("Handwritten Character Recognition")
root.geometry("400x300")

panel = tk.Label(root)
panel.pack(pady=10)

upload_btn = tk.Button(root, text="Upload Image", command=upload_image)
upload_btn.pack(pady=10)

result_label = tk.Label(root, text="Predicted Character:", font=('Helvetica', 16))
result_label.pack(pady=20)

root.mainloop()
