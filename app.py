# ------------------------------------------------------------
# 💖 Background Remover Web App - Pink Background with Purple Theme + Resize Feature
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
            backdrop-filter: blur(10px);
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
        .stImage:hover { transform: scale(1.02); }
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
    </style>
""", unsafe_allow_html=True)

# ------------------------------------------------------------
# PAGE TITLE
# ------------------------------------------------------------
st.markdown("<h1 class='main-title'>🖼️ AI Background Remover</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>Remove image backgrounds effortlessly and resize for social media 💜</p>", unsafe_allow_html=True)

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
    # RESIZE FEATURE
    # ------------------------------------------------------------
    st.markdown("### ✨ Resize for Social Media")
    platform = st.selectbox(
        "Choose a platform to resize your image for:",
        ["None", "Instagram", "Facebook", "WhatsApp"]
    )

    sizes = {
        "Instagram": (1080, 1080),
        "Facebook": (1200, 630),
        "WhatsApp": (640, 640)
    }

    resized_image = output_image

    if platform != "None":
        target_size = sizes[platform]
        resized_image = output_image.resize(target_size, Image.Resampling.LANCZOS)
        st.success(f"✅ Resized for {platform} ({target_size[0]}x{target_size[1]} px)")
        st.image(resized_image, caption=f"Resized for {platform}", use_column_width=True)

    # ------------------------------------------------------------
    # DOWNLOAD SECTION
    # ------------------------------------------------------------
    buf = io.BytesIO()
    resized_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button(
        label=f"📥 Download ({platform if platform != 'None' else 'Original Size'})",
        data=byte_im,
        file_name=f"output_{platform.lower() if platform!='None' else 'original'}.png",
        mime="image/png",
        use_container_width=True
    )

# ------------------------------------------------------------
# FOOTER
# ------------------------------------------------------------
st.markdown("<p class='footer'>Made with 💜 by Maham Waseem | Powered by Streamlit & Rembg</p>", unsafe_allow_html=True)
