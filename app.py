# ------------------------------------------------------------
# 🎨 Background Remover Web App - Modern Aesthetic Version
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
    initial_sidebar_state="expanded"
)

# ------------------------------------------------------------
# CUSTOM CSS STYLE
# ------------------------------------------------------------
st.markdown("""
    <style>
        /* Background color and text */
        body {
            background-color: #f7f9fb;
            color: #333333;
        }

        /* Main title style */
        .main-title {
            text-align: center;
            color: #4A90E2;
            font-size: 2.5em;
            font-weight: bold;
            margin-bottom: 10px;
        }

        /* Subtitle */
        .sub-title {
            text-align: center;
            color: #555555;
            font-size: 1.1em;
            margin-bottom: 30px;
        }

        /* Image container borders */
        .stImage {
            border-radius: 15px;
            box-shadow: 0px 4px 12px rgba(0,0,0,0.1);
        }

        /* Centered download button */
        .download-btn {
            display: flex;
            justify-content: center;
        }

        /* Footer */
        .footer {
            text-align: center;
            color: #888888;
            font-size: 0.9em;
            margin-top: 50px;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# PAGE TITLE
# ------------------------------------------------------------
st.markdown("<h1 class='main-title'>🖼️ AI Background Remover</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Upload your image and let AI remove the background instantly!</p>", unsafe_allow_html=True)

# ------------------------------------------------------------
# FILE UPLOAD
# ------------------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload an image file", type=["jpg", "jpeg", "png"])

if uploaded_file:
    input_image = Image.open(uploaded_file)

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Original Image")
        st.image(input_image, use_column_width=True)

    with st.spinner("✨ Removing background... Please wait..."):
        output_image = remove(input_image)

    with col2:
        st.subheader("Background Removed")
        st.image(output_image, use_column_width=True)

    # ------------------------------------------------------------
    # DOWNLOAD SECTION
    # ------------------------------------------------------------
    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.markdown("<div class='download-btn'>", unsafe_allow_html=True)
    st.download_button(
        label="📥 Download Image (PNG)",
        data=byte_im,
        file_name="output_image.png",
        mime="image/png",
        use_container_width=True
    )
    st.markdown("</div>", unsafe_allow_html=True)

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("<p class='footer'>Made with ❤️ using Streamlit and Rembg | © 2025 Maham Waseem</p>", unsafe_allow_html=True)
