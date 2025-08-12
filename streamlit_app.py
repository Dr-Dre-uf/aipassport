import streamlit as st
import cv2
import numpy as np

def apply_edge_detection(image, low_threshold, high_threshold):
    """Applies Canny edge detection to the image."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    edges = cv2.Canny(gray, low_threshold, high_threshold)
    return edges

def main():
    st.title("Image Edge Detection")

    # Image Upload
    uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

    if uploaded_file is not None:
        # Read the uploaded image
        img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    else:
        # Default image if no image is uploaded
        default_image = "assets/images/content/Identifying Structures in X-Ray Imaging.png"
        img = cv2.imread(default_image)
        
        if img is None:
            st.error(f"Could not load default image: {default_image}. Please make sure the file exists.")
            return
    
    # Sliders for thresholds
    low_threshold = st.slider("Low Threshold", 0, 200, 50)
    high_threshold = st.slider("High Threshold", 0, 255, 150)

    # Apply edge detection
    edges = apply_edge_detection(img, low_threshold, high_threshold)

    # Create columns for side-by-side display
    col1, col2 = st.column(2)

    # Display original image in the first column
    with col1:
        st.image(img, caption="Original Image", use_container_width=True)

    # Display edge-detected image in the second column
    with col2:
        st.image(edges, caption="Edge Detected Image", use_container_width=True)

if __name__ == "__main__":
    main()