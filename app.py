# ------------------------------------------------------------
# 🌈 Background Remover Web App - Gradient Aesthetic Version
# ------------------------------------------------------------
# Install (in case not done):
# pip install streamlit rembg pillow onnxruntime

import streamlit as st
from rembg import remove
from PIL import Image
import io

# ------------------------------------------------------------
# PAGE CONFIGURATION
# ------------------------------------------------------------
st.set_page_config(
    page_title="Background Remover App",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ------------------------------------------------------------
# CUSTOM GRADIENT CSS STYLE
# ------------------------------------------------------------
st.markdown("""
    <style>
        /* Gradient background */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #89f7fe 0%, #66a6ff 100%);
            color: #ffffff;
        }

        /* Sidebar (hidden by default) */
        [data-testid="stSidebar"] {
            background: #ffffffcc;
            backdrop-filter: blur(10px);
        }

        /* Title with glowing gradient text */
        .main-title {
            text-align: center;
            font-size: 3em;
            font-weight: 800;
            background: linear-gradient(90deg, #ff6a00, #ee0979, #0072ff);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        /* Subtitle */
        .sub-title {
            text-align: center;
            color: #f8f8f8;
            font-size: 1.2em;
            margin-bottom: 40px;
            font-weight: 400;
        }

        /* File uploader styling */
        .uploadedFile {
            border-radius: 10px !important;
            border: 2px dashed #ffffff !important;
            background-color: rgba(255,255,255,0.2);
            padding: 15px;
        }

        /* Image display cards */
        .stImage {
            border-radius: 20px !important;
            box-shadow: 0px 8px 25px rgba(0, 0, 0, 0.25);
            transition: transform 0.3s ease-in-out;
        }
        .stImage:hover {
            transform: scale(1.02);
        }

        /* Download button styling */
        div.stDownloadButton > button {
            background: linear-gradient(90deg, #0072ff, #00c6ff);
            color: white;
            border: none;
            padding: 0.8em 2em;
            font-size: 1.1em;
            border-radius: 12px;
            cursor: pointer;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.3);
            transition: all 0.3s ease-in-out;
        }

        div.stDownloadButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #ff6a00, #ee0979);
            box-shadow: 0px 4px 20px rgba(255, 255, 255, 0.4);
        }

        /* Footer */
        .footer {
            text-align: center;
            font-size: 0.95em;
            color: #f1f1f1;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# PAGE TITLE
# ------------------------------------------------------------
st.markdown("<h1 class='main-title'>🖼️ AI Background Remover</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Remove image backgrounds effortlessly using powerful AI — clean, fast, and beautiful.</p>", unsafe_allow_html=True)

# ------------------------------------------------------------
# FILE UPLOAD SECTION
# ------------------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload an image file", type=["jpg", "jpeg", "png"])

# ------------------------------------------------------------
# IMAGE PROCESSING
# ------------------------------------------------------------
if uploaded_file:
    input_image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("🎨 Original Image")
        st.image(input_image, use_column_width=True)

    with st.spinner("✨ Magic in progress... Removing background..."):
        output_image = remove(input_image)

    with col2:
        st.subheader("🌟 Background Removed")
        st.image(output_image, use_column_width=True)

    # ------------------------------------------------------------
    # DOWNLOAD SECTION
    # ------------------------------------------------------------
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label="📥 Download Image (PNG)",
        data=byte_im,
        file_name="output_image.png",
        mime="image/png",
        use_container_width=True
    )

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("<p class='footer'>Made with 💖 using Streamlit & Rembg | © 2025 Maham Waseem</p>", unsafe_allow_html=True)
