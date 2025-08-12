import streamlit as st
!pip install opencv-python
import cv2
import numpy as np
from PIL import Image

def edge_detection(image, low_threshold, high_threshold):
    """Performs edge detection on an image using the Canny edge detector."""
    gray = cv2.cvtColor(np.array(image), cv2.COLOR_BGR2GRAY)  # Convert PIL Image to NumPy array
    edges = cv2.Canny(gray, low_threshold, high_threshold)
    return edges

def main():
    """Main function to run the Streamlit app."""
    st.title("Edge Detection App")

    # Default image
    default_image = "https://www.easygifanimator.net/images/cases/video-to-gif-sample.gif"
    image = st.image(default_image, caption="Default Image", use_container_width=True)

    # Image upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])
    if uploaded_file is not None:
        image = Image.open(uploaded_file)  # Open as PIL Image
        if image is None:
            st.error("Error: Could not read the uploaded image. Please ensure it's a valid image file.")
            return

    # Threshold sliders
    low_threshold = st.slider("Low Threshold", 100, 255, 100)
    high_threshold = st.slider("High Threshold", 100, 255, 150)

    # Edge detection
    if image is not None:
        edges = edge_detection(image, low_threshold, high_threshold)

        with st.container():
            col1, col2 = st.columns(2)
            with col1:
                st.image(image, caption="Original Image", use_container_width=True)
            with col2:
                st.image(edges, caption="Edge Detected Image", use_container_width=True)


if __name__ == "__main__":
    main()
