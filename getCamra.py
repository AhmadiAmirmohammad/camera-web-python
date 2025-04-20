import streamlit as st
from PIL import Image

with st.expander('Camera App Demo'):
    # start camera
    camera_image = st.camera_input("Camera")

# print(camera_image)

if camera_image: # check this for not nall

    #creat a pillow image instance
    img = Image.open(camera_image)

    gray_image = img.convert('L')

    #Render the gray scale image
    st.image(gray_image)