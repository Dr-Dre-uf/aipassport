import streamlit as st
import cv2
import numpy as np
from PIL import Image

def edge_detection(image, threshold1, threshold2):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, threshold1, threshold2)
    return edges

st.title("Edge Detection Practice")

# Image Upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)

    # Edge Detection Parameters
    threshold1 = st.slider("Threshold 1", 0, 255, 100)
    threshold2 = st.slider("Threshold 2", 0, 255, 200)

    # Perform Edge Detection
    edges = edge_detection(image, threshold1, threshold2)

    # Display Images
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(edges, caption="Edge Detected Image", use_column_width=True)
