# <span style="font-size: 2em; font-weight: bold;">Handwritten Character Recognition</span>

## **Description**
- This project is a simple GUI-based application built using Python and TensorFlow to recognize handwritten characters from an uploaded image. The model was trained using a dataset of handwritten characters and is capable of predicting the character from a given input image.

---

## **Features**
- Easy-to-use graphical interface.
- Predicts handwritten characters from image uploads.
- Pre-trained model for character recognition.

---

## **Prerequisites**
- Python 3.x
- TensorFlow
- NumPy
- Pillow (PIL)

---

## **Installation**
1. Clone the repository:
   - `git clone https://github.com/Anshul00910/Handwritten_Character_Recognition.git`
   - `cd your-repo`

2. Install required packages:
   - `pip install -r requirements.txt`

3. Ensure the pre-trained model (`handwritten_character_recognition_model.h5`) and class labels (`class_labels.json`) are in the repository's root directory.

---

## **Usage**
1. Run the script:
   - `python app.py`

2. A GUI window will appear. Upload an image of a handwritten character, and the application will display the predicted character.

---

## **File Structure**
- `app.py`: Main script that runs the application and performs character recognition.
- `handwritten_character_recognition_model.h5`: Pre-trained model for character recognition.
- `class_labels.json`: JSON file mapping numeric labels to character classes.

---

## **Contributing**
- Contributions are welcome! Feel free to fork the repository and create a pull request.

