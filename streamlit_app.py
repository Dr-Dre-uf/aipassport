import streamlit as st
import cv2
import numpy as np

def apply_edge_detection(image, algorithm, low_threshold=50, high_threshold=150):
    """Applies edge detection to the image using the specified algorithm."""
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    if algorithm == "Canny":
        edges = cv2.Canny(gray, low_threshold, high_threshold)
    elif algorithm == "Laplacian":
        edges = cv2.Laplacian(gray, cv2.CV_64F)
        edges = np.uint8(np.absolute(edges))
    elif algorithm == "Sobel":
        sobelx = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=5)
        sobely = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=5)
        edges = np.sqrt(sobelx**2 + sobely**2)
        edges = np.uint8(edges)
    else:
        raise ValueError("Invalid edge detection algorithm")

    # Convert to 3-channel image
    edges = cv2.cvtColor(edges, cv2.COLOR_GRAY2BGR)

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
    
    # Algorithm selection
    algorithm = st.selectbox("Edge Detection Algorithm", ["Canny", "Laplacian", "Sobel"])

    # Sliders for thresholds (only for Canny)
    if algorithm == "Canny":
        low_threshold = st.slider("Low Threshold", 0, 200, 50)
        high_threshold = st.slider("High Threshold", 0, 255, 150)
    else:
        low_threshold = 0
        high_threshold = 0

    # Apply edge detection
    edges = apply_edge_detection(img, algorithm, low_threshold, high_threshold)

    # Slider for blending
    alpha = st.slider("Blending", 0.0, 1.0, 0.5)

    # Blend the images
    blended_image = cv2.addWeighted(img, 1 - alpha, edges, alpha, 0)

    # Display original, edge-detected, and blended images
    st.image([img, edges, blended_image], caption=["Original Image", "Edge Detected Image", "Blended Image"], use_column_width=True)

if __name__ == "__main__":
    main()