import streamlit as st
import numpy as np
from PIL import Image
from skimage import filters

def edge_detection(image, low_threshold, high_threshold):
    """Applies Canny edge detection using scikit-image."""
    edges = filters.canny(image, low_threshold=low_threshold, high_threshold=high_threshold)
    return edges

st.title("Edge Detection Practice (Scikit-image)")

# Default Image
default_image = "assets/images/content/Identifying Structures in X-Ray Imaging.png"  # Replace with the actual filename you uploaded

# Image Upload
uploaded_file = st.file_uploader("Upload an image (optional)", type=["jpg", "jpeg", "png"])

# Load Image (uploaded or default)
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    image = np.array(image)
else:
    image = Image.open(default_image)
    image = np.array(image)

# Edge Detection Parameters
low_threshold = st.slider("Low Threshold", 0, 255, 50)
high_threshold = st.slider("High Threshold", 0, 255, 150)

# Perform Edge Detection
edges = edge_detection(image, low_threshold, high_threshold)

# Display Images
st.image(image, caption="Original Image", use_container_width=True)
st.image(edges, caption="Edge Detected Image", use_container_width=True)
