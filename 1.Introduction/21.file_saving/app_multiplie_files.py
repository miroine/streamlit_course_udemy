import streamlit as st
import pandas as pd
import numpy as np
import os 
# file processing pkgs
from PIL import Image


@st.cache_data
def load_image(image_file):
    """Return an Image object

    Args:
        image_file (_type_): _description_

    Returns:
        _type_: _description_
    """
    img = Image.open(image_file)
    return img

def save_uploaded_file(uploaded_file):
    with open(os.path.join("tempDir", uploaded_file.name), 'wb') as f:
        f.write(uploaded_file.getbuffer()) 
    return st.success(f"saved {uploaded_file.name}")

def main():
    st.title("File Upload Tutorial")
    
    menu = ["Home","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Upload mulitplie files")
        uploadedfiles = st.file_uploader("Upload Multiplie Images",
                                         type=["png","jpg","jpeg"],
                                         accept_multiple_files=True)
        if uploadedfiles:
            for imagefile in uploadedfiles:
                st.write(imagefile.name)
                st.image(load_image(imagefile), width= 250)
                #save individual files
                save_uploaded_file(imagefile)                


        
    
    else:
        st.subheader("About") 
    
    
    



if __name__ == '__main__':
    main()