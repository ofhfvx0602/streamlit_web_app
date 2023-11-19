import streamlit as st
from PIL import Image

st.title('test app')
st.caption('Test Web App')

image = Image.open('./data/anonymous.png')
st.image(image, width=200)







