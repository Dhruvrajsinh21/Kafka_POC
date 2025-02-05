import streamlit as st
import os
from producer import send_image_to_kafka  
import time

UPLOAD_FOLDER = "uploads/"
THUMBNAIL_FOLDER = "thumbnails/"

os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(THUMBNAIL_FOLDER, exist_ok=True)

if 'image_sent' not in st.session_state:
    st.session_state.image_sent = False
if 'uploaded_image' not in st.session_state:
    st.session_state.uploaded_image = None
if 'thumbnail' not in st.session_state:
    st.session_state.thumbnail = None

st.title("Kafka Image Processing with Thumbnails")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"], key="image_uploader")

if uploaded_file is not None:
    if st.session_state.uploaded_image:
        os.remove(st.session_state.uploaded_image)
        st.session_state.image_sent = False
        st.session_state.thumbnail = None 

    image_path = os.path.join(UPLOAD_FOLDER, uploaded_file.name)
    with open(image_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.uploaded_image = image_path
    st.session_state.image_sent = False 
    st.session_state.thumbnail = None

    st.success(f"Uploaded {uploaded_file.name}")

if st.session_state.uploaded_image and not st.session_state.image_sent:
    send_image_to_kafka(st.session_state.uploaded_image)
    st.session_state.image_sent = True
    st.success(f"Image {uploaded_file.name} sent to Kafka for processing!")

st.subheader("Processed Images")

if st.session_state.uploaded_image:
    original_path = st.session_state.uploaded_image
    thumbnail_path = os.path.join(THUMBNAIL_FOLDER, os.path.basename(original_path).split('.')[0] + "_thumbnail.jpg")
    thumbnail_generated = False
    while not thumbnail_generated:
        if os.path.exists(thumbnail_path):
            thumbnail_generated = True
        else:
            time.sleep(1)
    col1, col2 = st.columns(2)
    with col1:
        st.image(original_path, caption="Original", width=250)
    with col2:
        st.image(thumbnail_path, caption="Thumbnail", width=200)
