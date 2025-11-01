# ------------------------------------------------------------
# 💜 Background Remover Web App - Purple Gradient Theme
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
# CUSTOM PURPLE THEME CSS STYLE
# ------------------------------------------------------------
st.markdown("""
    <style>
        /* Gradient background - Purple aesthetic */
        [data-testid="stAppViewContainer"] {
            background: linear-gradient(135deg, #6a11cb 0%, #2575fc 100%);
            color: #ffffff;
        }

        /* Sidebar */
        [data-testid="stSidebar"] {
            background: #ffffffcc;
            backdrop-filter: blur(10px);
        }

        /* Title styling */
        .main-title {
            text-align: center;
            font-size: 3em;
            font-weight: 800;
            background: linear-gradient(90deg, #b993d6, #8ca6db);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 5px;
            text-shadow: 2px 2px 4px rgba(0,0,0,0.2);
        }

        /* Subtitle */
        .sub-title {
            text-align: center;
            color: #e5e5f7;
            font-size: 1.2em;
            margin-bottom: 40px;
            font-weight: 400;
        }

        /* File uploader */
        .uploadedFile {
            border-radius: 10px !important;
            border: 2px dashed #d1c4e9 !important;
            background-color: rgba(255,255,255,0.15);
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

        /* Download button */
        div.stDownloadButton > button {
            background: linear-gradient(90deg, #6a11cb, #2575fc);
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
            background: linear-gradient(90deg, #8e2de2, #4a00e0);
            b
