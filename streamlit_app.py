import streamlit as st
import cv2
import numpy as np

# --- PAGE CONFIG & PRIVACY WARNING ---
st.set_page_config(page_title="AI Passport: Clinical Demo", layout="wide")

st.sidebar.warning("PRIVACY NOTICE: Please do not upload any images containing Protected Health Information (PHI) or sensitive personal data.")

st.sidebar.title("AI Passport: Clinical Assignment")
activity = st.sidebar.radio(
    "Select Activity:", 
    ["Activity 1: X-ray Edge Detection", "Activity 2: CT vs MRI Analysis"],
    help="Use this menu to navigate between the different parts of your clinical assignment."
)

# --- SHARED FUNCTIONS ---
def apply_edge_detection(image, low, high):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return cv2.Canny(gray, low, high)

def adjust_contrast_brightness(image, contrast, brightness):
    # contrast: 1.0-3.0, brightness: 0-100
    return cv2.convertScaleAbs(image, alpha=contrast, beta=brightness)

# --- ACTIVITY 1: X-RAY ---
if activity == "Activity 1: X-ray Edge Detection":
    st.title("Activity 1: Identifying Structures in X-Ray Imaging")
    
    st.markdown("""
    **Clinical Scenario:** A 28-year-old male presents to the emergency department following a skiing accident. He reports pain in his lower leg. An X-ray is ordered to assess for potential fractures to the tibia and fibula. The X-ray reveals potential damage, but identifying a fracture is proving difficult.
    
    **Instructions:**
    1. Observe the default X-ray image below or upload your own sample image.
    2. Adjust the **Low Threshold** and **High Threshold** sliders.
    3. Observe how the edge detection algorithm highlights different structures and noise within the image.
    4. Return to Canvas to answer the question: *Why might edge detection alone be insufficient for detecting fractures in an X-ray image?*
    """)
    
    uploaded_file = st.file_uploader(
        "Upload an X-ray (Optional)", 
        type=["jpg", "jpeg", "png"], 
        key="xray_up",
        help="Upload a standard image file (JPG or PNG). Ensure no patient data is visible."
    )

    if uploaded_file:
        img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    else:
        # Placeholder for your default fracture image
        default_path = "assets/images/content/Identifying Structures in X-Ray Imaging.png"
        img = cv2.imread(default_path)
        if img is None:
            st.error("Please upload an image to begin, or ensure the default image is placed in the correct directory.")
            st.stop()

    st.markdown("### Image Processing Controls")
    low_threshold = st.slider(
        "Low Threshold (Sensitivity)", 
        0, 200, 100,
        help="Pixels with an intensity gradient below this value will be discarded. Lowering this increases the noise detected."
    )
    high_threshold = st.slider(
        "High Threshold (Edge Strength)", 
        0, 255, 150,
        help="Pixels with an intensity gradient above this value are marked as strong edges. Adjust this to isolate distinct boundaries."
    )
    
    edges = apply_edge_detection(img, low_threshold, high_threshold)

    col1, col2 = st.columns(2)
    col1.image(img, caption="Original X-ray", use_container_width=True)
    col2.image(edges, caption="Edge Detection Output", use_container_width=True)

# --- ACTIVITY 2: CT vs MRI ---
elif activity == "Activity 2: CT vs MRI Analysis":
    st.title("Activity 2: Comparing CT and MRI for Brain Imaging")
    
    st.markdown("""
    **Clinical Scenario:** CT and MRI scans are commonly used for brain imaging to diagnose different conditions based on tissue density and composition.
    
    **Instructions:**
    1. Observe the medical scans provided below.
    2. Use the **Contrast** and **Brightness** sliders to simulate how a radiologist might adjust viewing parameters ("windowing").
    3. Notice how adjusting these settings impacts the visibility of dense structures (like bone) versus soft tissues.
    4. Return to Canvas to list the key differences between the modalities and explain their preferred clinical scenarios.
    """)
    
    uploaded_file = st.file_uploader(
        "Upload a Brain Scan (Optional)", 
        type=["jpg", "jpeg", "png"], 
        key="brain_up",
        help="Upload a standard image file (JPG or PNG). Ensure no patient data is visible."
    )

    if uploaded_file:
        img = cv2.imdecode(np.frombuffer(uploaded_file.read(), np.uint8), cv2.IMREAD_COLOR)
    else:
        # Default side-by-side comparison image
        default_path = "assets/images/content/CT_MRI_Comparison.png" 
        img = cv2.imread(default_path)
        if img is None:
            st.error("Please upload a scan to begin, or ensure the default comparison image is in the correct directory.")
            st.stop()

    st.markdown("### Interactive Tissue Contrast Adjustment")
    
    col_ctrl1, col_ctrl2 = st.columns(2)
    with col_ctrl1:
        contrast = st.slider(
            "Increase Contrast (Intensity)", 
            1.0, 3.0, 1.2,
            help="Increases the visual difference between the light and dark areas of the scan, helping to distinguish between tissue types."
        )
    with col_ctrl2:
        brightness = st.slider(
            "Brightness", 
            -50, 50, 0,
            help="Adjusts the overall lightness or darkness of the image to reveal hidden details in shadowed areas."
        )

    adjusted_img = adjust_contrast_brightness(img, contrast, brightness)

    st.image(adjusted_img, caption="Adjusted Scan View", use_container_width=True)
    
    st.info("Observation Tip for Canvas: Notice how the CT scan loses detail in the brain tissue when contrast is high, but the bone remains distinct. Conversely, observe how the MRI retains distinct layers of soft tissue.")
