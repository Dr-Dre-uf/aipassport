import streamlit as st
import cv2
import numpy as np

def main():
    st.title("Image Edge Detection")

    # Default image
    default_image = "default_image.jpg"  # Replace with your image file
    img = cv2.imread(default_image)
    
    if img is None:
        st.error(f"Could not load default image: {default_image}. Please make sure the file exists.")
        return

    st.image(img, caption="Original Image", use_column_width=True)

if __name__ == "__main__":
    main()