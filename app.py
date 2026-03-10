import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Brain Tumor Detection", layout="centered")

st.title("🧠 Brain Tumor Detection")
st.write("Select an MRI image and get prediction")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("brain_tumor_mobilenet_fixed.keras",compile=False)

model = load_model()
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input
def preprocess_image(image):
    image = image.convert("RGB")
    image = image.resize((224, 224))
    image = np.array(image) #/ 255.0
    image = np.expand_dims(image, axis=0)
    return image

image_file = st.file_uploader(
    "Choose MRI Image",
    type=["jpg", "jpeg", "png"]
)

if image_file is not None:
    image = Image.open(image_file)
    st.image(image, caption="Selected MRI Image", use_column_width=True)

    img = preprocess_image(image)
    prediction = model.predict(img)[0][0]
    score = prediction

    st.write(f"Raw prediction score: {score:.4f}")

    if score > 0.45:
        st.success("✅ No Tumor Detected")
    elif score <0.4:
        st.error("🧠 Tumor Detected")
    else:
        st.warning("⚠️ Uncertain result. Further medical analysis required.")

    # prediction = model.predict(img)[0][0]
    # st.write(f"Raw prediction score: {prediction:.4f}")

    # if prediction > 0.6:
    #     st.error(f"🧠 Tumor Detected ({prediction*100:.2f}%)")
    # else:
    #     st.success(f"✅ No Tumor Detected ({(1-prediction)*100:.2f}%)")


    # #tumout yes - 0.5643 ,0.5758 ,0.5668 ,0.5599 ,0.5746
     #tumout no -  0.5601 ,0.5641 ,0.5599 ,0.5590