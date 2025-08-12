import streamlit as st
import numpy as np
from PIL import Image
from skimage import filters

def edge_detection(image, sigma):
    """Applies Sobel edge detection using scikit-image."""
    edges = filters.sobel(image)
    return edges

st.title("Edge Detection Practice (Scikit-image)")

# Image Upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)
    image = np.array(image)  # Convert to NumPy array

    # Edge Detection Parameters
    sigma = st.slider("Sigma (for Sobel filter)", 0.0, 5.0, 1.0)

    # Perform Edge Detection
    edges = edge_detection(image, sigma)

    # Display Images
    st.image(image, caption="Original Image", use_column_width=True)
    st.image(edges, caption="Edge Detected Image", use_column_width=True)
