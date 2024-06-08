import streamlit as st  
import streamlit.components as stc 

#UTILS 
import base64 
import time 
import pandas as pd 

timestr = time.strftime("%Y%m%d-%H%M%S")

#Fxn  
def text_downloader(raw_text):
    b64 = base64.b64encode(raw_text.encode()).decode()
    new_filename = f"new_text_file_{timestr}.txt"
    st.markdown("######### Dowload File #########")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}" download="{new_filename}">Download File</a>'
    st.markdown(href, unsafe_allow_html=True)

def csv_downloader(data):
    csv_file = data.to_csv()
    b64 = base64.b64encode(csv_file.encode()).decode()
    new_filename = f"new_text_file_{timestr}.txt"
    st.markdown("######### Dowload File #########")
    href = f'<a href="data:file/txt;base64,{b64}" download="{new_filename}" download="{new_filename}">Download File</a>'
    st.markdown(href, unsafe_allow_html=True)

#class  
class FileDownloader(object):
    def __init__(self,data, filename ="myfile", file_ext = 'txt'):
        super(FileDownloader,self).__init__()
        self.data = data
        self.filename = filename 
        self.extension = file_ext 
    
    def download(self):
        b64 = base64.b64encode(self.data.encode()).decode()
        new_filename = f"new_text_file_{timestr}.{self.extension}"
        st.markdown("######### Dowload File #########")
        href = f'<a href="data:file/{self.extension};base64,{b64}" download="{new_filename}" download="{new_filename}">Download File</a>'
        st.markdown(href, unsafe_allow_html=True) 


def main():
    menu =["Home", "CSV", "About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        my_text = st.text_area("Enter Text")
        if st.button("Save"):
            st.write(my_text)
            #text_downloader(my_text)
            download = FileDownloader(my_text).download()
    if choice == "CSV":
        df = pd.read_csv("Iris.csv")
        st.dataframe(df.head())
        download = FileDownloader(df.to_csv()).download() 




if __name__ == "__main__":
    main()
    