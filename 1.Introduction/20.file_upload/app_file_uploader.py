import streamlit as st
import pandas as pd
import numpy as np

# file processing pkgs
from PIL import Image
import docx2txt
from PyPDF2 import PdfReader
import pdfplumber


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

def read_pdf(file):
    """Read PDF file

    Args:
        file (_type_): _description_

    Returns:
        _type_: _description_
    """
    pdfReader = PdfReader(file)
    count = len(pdfReader.pages)
    all_page_text = ""
    for i in range(count):
        page = pdfReader.pages[i]
        all_page_text += page.extract_text()

    return all_page_text

def main():
    st.title("File Upload Tutorial")
    
    menu = ["Home","Dataset","DocumentFiles","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images", type=["png","jpg","jpeg"])
        if image_file is not None:
            #st.write(type(image_file))
            #st.write (dir(image_file))
            
            file_details = {"filename":image_file.name,
                            "filetype":image_file.type,
                            "filesize":image_file.size}
            st.write(file_details)
            st.image(load_image(image_file), width= 250)
        
        
    elif choice == "Dataset":
        st.subheader("Dataset") 
        data_file = st.file_uploader("Upload CSV", 
                                     type=["csv"])
        if data_file :
            #st.write(type(data_file))
            file_details = {"filename":data_file.name,
                            "filetype":data_file.type,
                            "filesize":data_file.size}   
            st.write(file_details)
            df = pd.read_csv(data_file) 
            st.dataframe(df)     
    elif choice == "DocumentFiles":
        st.subheader("DocumentFiles")
        docs_file = st.file_uploader("Upload Document", 
                                     type=["pdf","docx","txt"])
        if st.button("Process"):
            if docs_file:
                
                file_details = {"filename":docs_file.name,
                                "filetype":docs_file.type,
                                "filesize":docs_file.size}
                st.write(file_details)
                if docs_file.type == "text/plain":
                    raw_text = str(docs_file.read(),"utf-8")
                    st.write(raw_text)
                elif docs_file.type == "application/pdf":
                    raw_text = read_pdf(docs_file)
                    st.write(raw_text)
        
    
    else:
        st.subheader("About") 
    
    
    



if __name__ == '__main__':
    main()


