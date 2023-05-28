import streamlit as st
import os
from PIL import Image
import cv2
import numpy as np
from io import BytesIO, StringIO
import subprocess

st.set_page_config(layout="wide", page_title="YOLOv5 Crash Detection")

@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

with st.container():
    st.title("This will help us to get the data from you in case of any accident you encounter (road accident and fire accident).")

with st.container():
    try:
        image_file = st.file_uploader("Choose a image file", type=["jpg", "jpeg", "png"])
        if image_file is not None:
            with open(image_file.name,"wb") as f:
                f.write(image_file.getbuffer())
                result = subprocess.run(['python', 'crash_code.py', '--source', f'{image_file.name}'])
                print(result.stdout)
                #os.popen(f"fire_smoke_detect_prod.py --source {image_file.name}")
                #exec(open(f"fire_smoke_detect_prod.py --source {image_file.name}").read())

            st.success("done saving")

    except Exception as e:
        st.write(e)