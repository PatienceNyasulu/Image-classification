import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf

# Load your trained model
@st.cache_resource
def load_model():
    return tf.keras.models.load_model("classifier_model1.keras")  

model = load_model()

# Streamlit UI
st.set_page_config(page_title="Image Classifier", layout="centered")

st.markdown("""
    <style>
        .main { background-color: #f8f9fa; }
        .title { text-align: center; color: #4a4a4a; font-size: 40px; }
    </style>
""", unsafe_allow_html=True)

st.markdown('<div class="title">🖼️ Image Classifier</div>', unsafe_allow_html=True)
st.write("Upload an image below (max 5MB). The model will predict its class.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])


if uploaded_file is not None:
    # Check file size (in MB)
    uploaded_file.seek(0, 2)
    file_size_mb = uploaded_file.tell() / (1024 * 1024)
    uploaded_file.seek(0)

    if file_size_mb > 5:
        st.error("File size exceeds 5MB limit.")
    else:
        image = Image.open(uploaded_file).convert("RGB")
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocessing (Update this to match your CNN model's input shape)
        img = image.resize((224, 224))  # Modify size as required
        img_array = np.array(img) / 255.0
        #img_array = np.expand_dims(img_array, axis=0)

        if img_array.shape[-1] != 3:
           st.error("Image is not in RGB format.")
        else:
           img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension


        if st.button("Classify"):
            prediction = model.predict(img_array)
            class_idx = np.argmax(prediction, axis=1)[0]

            # Replace with actual class names from your model
            class_names = ['airplane', 'automobile', 'bird', 'cat', 'deer', 
          'dog', 'frog', 'horse', 'ship', 'truck']
            st.success(f"Predicted Class: **{class_names[class_idx]}**")
            
