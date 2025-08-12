import streamlit as st
import cv2
import numpy as np

# Default image
default_image = "assets/images/content/Identifying Structures in X-Ray Imaging.png"

# Load the default image
img = cv2.imread(default_image)
if img is None:
    st.error("Error loading default image. Please check the URL.")
    st.stop()
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Image upload
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    img = cv2.imread(uploaded_file)
    if img is None:
        st.error("Error loading uploaded image. Please check the file type.")
        st.stop()
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Sliders for threshold values
low_threshold = st.slider("Low Threshold", 0, 255, 50)
high_threshold = st.slider("High Threshold", 0, 255, 150)

# Edge detection
edges = cv2.Canny(img, low_threshold, high_threshold)

# Slider to compare original and edge-detected image
comparison_slider = st.slider(
    "Compare Original vs. Edge Detected",
    0.0, 1.0, 0.5
)

# Combine images for comparison
combined_image = cv2.addWeighted(img, 1 - comparison_slider, edges, comparison_slider, 0)

# Display images
st.image([img, combined_image], caption=["Original Image", "Edge Detected Image"])