# app.py
import streamlit as st
import numpy as np
from PIL import Image, UnidentifiedImageError
import requests
from io import BytesIO
from requests.models import MissingSchema

from utils.classifier import load_model, classify

st.title("OpenCV DNN Image Classification")

@st.cache_resource
def load():
    return load_model()

net, class_names = load()

img_file_buffer = st.file_uploader("Choose a file or Camera", type=['jpg', 'jpeg', 'png'])
st.text('OR')
url = st.text_input('Enter Image URL')

def header(text):
    st.markdown(
        f'<p style="background-color:#111111;color:#33ff33;font-size:24px;'
        f'border-radius:5px;padding:10px;" align="center">{text}</p>',
        unsafe_allow_html=True)

if img_file_buffer is not None:
    image = np.array(Image.open(img_file_buffer))
    st.image(image)
    result = classify(net, image, class_names)
    header(result)

elif url != '':
    try:
        response = requests.get(url)
        image = np.array(Image.open(BytesIO(response.content)))
        st.image(image)
        result = classify(net, image, class_names)
        header(result)
    except MissingSchema:
        st.header('Invalid URL. Try again.')
    except UnidentifiedImageError:
        st.header('URL has no image. Try again.')
