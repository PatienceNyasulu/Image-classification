# 🖼️ Streamlit Image Classifier

This project is a simple and elegant web application built with [Streamlit](https://streamlit.io/) that allows users to upload an image (max 5MB) and receive a predicted class using a Convolutional Neural Network (CNN) model trained in TensorFlow/Keras.

## 🚀 Features

- Upload image files (`.jpg`, `.jpeg`, `.png`)
- File size validation (max 5MB)
- Real-time image preview
- CNN-based image classification
- Clean and minimalistic UI

## 📁 Project Structure

├── app.py # Streamlit app
├── your_model.h5 # Trained CNN model
├── requirements.txt # Python dependencies
└── README.md # Project description


## 🔧 Setup Instructions

### 1. Clone the Repository
```
git clone https://github.com/your-username/streamlit-image-classifier.git
cd streamlit-image-classifier
```
###2. Create a Virtual Environment (Recommended)
```
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
```
###3. Install Dependencies
```
pip install -r requirements.txt
```
###4. Add Your Model
#Make sure your trained model (your_model.h5) is in the project directory.

###5. Run the Streamlit App
```
streamlit run app.py
```
###🧠 Model Information
The model used in this project is a Convolutional Neural Network (CNN) trained to classify images into predefined categories. Update the class labels and image preprocessing logic in app.py to match your model’s configuration.

###📷 Example
<!-- Optional: Add a screenshot image to your repo -->
