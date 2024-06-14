# Core Pkgs
import streamlit as st 
import streamlit.components.v1 as stc

#EDA Pkgs 
import pandas as pd
import numpy as np

# User packages

from utils.get_data import get_data_from_uci

# importing the apps 
from apps.eda_app import run_eda_app
from apps.ml_app import run_ml_app


app_title = "Early Stage Diabetes Risk Predictor"
app_subtitle = "Predicting the risk of diabetes based on the given parameters"
HTML_BANNER = f"""
    <div style="background-color: #464e5f; padding: 10px; border-radius: 10px;">
    <h1 style="color: white; font-size: 30px; text-align: center;">{app_title}</h1>
    </div>
"""

HTML_TEMPLATE = f""" 
    <div style="background-color: #3872fb; padding: 10px; border-radius: 10px;">
    <h1 style="color: white; font-size: 30px; text-align: center;">{app_title}</h1>
    <h4 style="color: white; text-align: center;">{app_subtitle}</h4>
    </div>"""

desc_temp = """
            ### Early Stage Diabetes Risk Predictor App
            This dataset contains the sign and symptoms data for new diabetes patients.
            ### Datasource: 
                - https://archive.ics.uci.edu/ml/datasets/Early+stage+diabetes+risk+prediction+(2020)
            #### App Contents
                - EDA Section: Exploratory Data Analysis
                - ML Section: Machine Learning Applications
"""

# Main script
def main():
    stc.html(HTML_BANNER, height=100)

    
    choice = st.sidebar.selectbox("Menu", ["Home","EDA", "ML", "About"])
    if choice == "Home":
        st.subheader("Home")
        stc.html(HTML_TEMPLATE, height=200)
        st.markdown(desc_temp, unsafe_allow_html=True)
    if choice == "EDA":
        run_eda_app()
    elif choice == "ML":
        run_ml_app()
    else:
        st.subheader("About")


if __name__ == "__main__":
    main()