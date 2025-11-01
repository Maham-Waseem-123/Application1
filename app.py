# ------------------------------------------------------------
# 💖 AI Background Remover - Pink & Purple Edition (Enhanced)
# ------------------------------------------------------------
# Install first (if not done):
# pip install streamlit rembg pillow onnxruntime

import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
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
# CUSTOM STYLE (Pink Background + Purple Writeup)
# ------------------------------------------------------------
st.markdown("""
    <style>
        [data-testid="stAppViewContainer"] {
            background-color: #ffe6f2;
            color: #5a00b0;
        }

        [data-testid="stSidebar"] {
            background: rgba(255, 240, 250, 0.9);
            color: #5a00b0;
        }

        .main-title {
            text-align: center;
            font-size: 3em;
            font-weight: 800;
            color: #7b2cbf;
            margin-bottom: 5px;
            text-shadow: 1px 1px 3px rgba(0,0,0,0.1);
        }

        .sub-title {
            text-align: center;
            color: #9d4edd;
            font-size: 1.2em;
            margin-bottom: 40px;
            font-weight: 400;
        }

        .stImage {
            border-radius: 20px !important;
            box-shadow: 0px 8px 25px rgba(123, 44, 191, 0.3);
            transition: transform 0.3s ease-in-out;
        }

        .stImage:hover {
            transform: scale(1.02);
        }

        div.stDownloadButton > button {
            background: linear-gradient(90deg, #9d4edd, #7b2cbf);
            color: white;
            border: none;
            padding: 0.8em 2em;
            font-size: 1.1em;
            border-radius: 12px;
            cursor: pointer;
            box-shadow: 0px 4px 15px rgba(0, 0, 0, 0.25);
            transition: all 0.3s ease-in-out;
        }

        div.stDownloadButton > button:hover {
            transform: scale(1.05);
            background: linear-gradient(90deg, #7b2cbf, #5a00b0);
            box-shadow: 0px 4px 25px rgba(155, 0, 255, 0.4);
        }

        .footer {
            text-align: center;
            font-size: 0.95em;
            color: #7b2cbf;
            margin-top: 40px;
        }

        hr {
            border: none;
            height: 2px;
            background: linear-gradient(to right, #ffb3e6, #c77dff);
            margin: 25px 0;
        }
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# PAGE HEADER
# ------------------------------------------------------------
st.markdown("<h1 class='main-title'>🖼️ AI Background Remover</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Remove image backgrounds effortlessly using AI — pink & purple aesthetic 💜</p>", unsafe_allow_html=True)

# ------------------------------------------------------------
# FILE UPLOAD SECTION
# ------------------------------------------------------------
uploaded_file = st.file_uploader("📤 Upload an image file", type=["jpg", "jpeg", "png"])

# ------------------------------------------------------------
# IMAGE PROCESSING
# ------------------------------------------------------------
if uploaded_file:
    input_image = Image.open(uploaded_file).convert("RGBA")

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("🎨 Original Image")
        st.image(input_image, use_column_width=True)

    with st.spinner("✨ Removing background..."):
        output_image = remove(input_image)

    # ------------------------------------------------------------
    # BACKGROUND PREVIEW OPTIONS
    # ------------------------------------------------------------
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("🌈 Preview Background Options")

    bg_option = st.radio("Choose a background:", ["Transparent", "White", "Black", "Custom Color"])

    if bg_option == "White":
        bg_color = (255, 255, 255, 255)
    elif bg_option == "Black":
        bg_color = (0, 0, 0, 255)
    elif bg_option == "Custom Color":
        hex_color = st.color_picker("🎨 Pick a background color", "#FFC0CB")
        bg_color = tuple(int(hex_color.lstrip('#')[i:i+2], 16) for i in (0, 2, 4)) + (255,)
    else:
        bg_color = None

    # Apply background color if selected
    if bg_color:
        bg_layer = Image.new("RGBA", output_image.size, bg_color)
        output_image = Image.alpha_composite(bg_layer, output_image)

    with col2:
        st.subheader("🌟 Background Removed")
        st.image(output_image, use_column_width=True)

    # ------------------------------------------------------------
    # DOWNLOAD SECTION
    # ------------------------------------------------------------
    st.markdown("<hr>", unsafe_allow_html=True)
    st.subheader("📥 Download Options")

    file_format = st.radio("Choose download format:", ["PNG", "JPG"])
    buf = io.BytesIO()

    if file_format == "PNG":
        output_image.save(buf, format="PNG")
        file_name = "background_removed.png"
        mime_type = "image/png"
    else:
        output_image = output_image.convert("RGB")
        output_image.save(buf, format="JPEG")
        file_name = "background_removed.jpg"
        mime_type = "image/jpeg"

    st.download_button(
        label=f"📥 Download {file_format} Image",
        data=buf.getvalue(),
        file_name=file_name,
        mime=mime_type,
        use_container_width=True
    )

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("<p class='footer'>Made with 💜 by Maham Waseem | Powered by Streamlit & Rembg</p>", unsafe_allow_html=True)
