import streamlit as st
from rembg import remove
from PIL import Image
import io

st.title("🖼️ Background Remover App")
uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    input_image = Image.open(uploaded_file)
    st.image(input_image, caption="Original Image", use_column_width=True)

    with st.spinner("Removing background..."):
        output_image = remove(input_image)

    st.image(output_image, caption="Image Without Background", use_column_width=True)

    buf = io.BytesIO()
    output_image.save(buf, format="PNG")
    byte_im = buf.getvalue()

    st.download_button("📥 Download PNG", data=byte_im, file_name="output_image.png", mime="image/png")
