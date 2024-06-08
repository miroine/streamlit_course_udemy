import streamlit as st 
import pandas as pd
import time


def load_data(data):
    return pd.read_csv(data)

timestr = time.strftime("%Y%m%d-%H%M%S")
def main():
    st.title("Streamlit Editor App")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        data_file = st.file_uploader("Upload CSV File", 
                                     type=["csv"])
        if data_file: 
            df = load_data(data_file)
            # Saving form 
            with st.form("editor_form"):
                df_edit = st.data_editor(df)
                save_button = st.form_submit_button(label="Save Data")
                #st.write(dir(data_file))
            if save_button:
                new_filename = f"{data_file.name}_{timestr}.csv"
                st.download_button(label="Download Data as Csv", 
                                    data=df_edit.to_csv(), file_name=new_filename)
                st.success("Data Saved Successfully")
                st.dataframe(df_edit.head())
    else:
        st.subheader("About")
    

if __name__ == "__main__":
    main()