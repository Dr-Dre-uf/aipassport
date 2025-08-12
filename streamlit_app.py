import streamlit as st
import cv2
import numpy as np

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
    
    st.image(img, caption="Original Image", use_container_width=True)

if __name__ == "__main__":
    main()