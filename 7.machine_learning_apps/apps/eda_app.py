import streamlit as st 
import streamlit.components.v1 as stc

from utils.get_data import *

#EDA Pkgs 
import pandas as pd
import numpy as np

# Load data Viz Pkgs 
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import plotly.express as px

matplotlib.use("agg")


HTML_BANNER = """
    <div style="background-color: #464e5f; padding: 10px; border-radius: 10px;">
    <h1 style="color: white; font-size: 30px; text-align: center;">Early Stage DM Risk Data Analysis</h1>
    </div>
"""
@st.cache_data()
def get_data():
    df = get_data_from_uci()
    return df

def load_data():
        data =st.file_uploader("Upload your file", type=["csv"])
        try:
            df = pd.read_csv(data)  
        except:
            st.error("Please upload a csv file")
            st.stop()
        return df

        
# Main script
def run_eda_app():

    st.subheader("EDA")
    st.write("This application predicts the risk of diabetes based on the given parameters")
    choice = st.sidebar.selectbox("data loading", ["online","local"])
    if choice == "local":
        df=load_data()
    else:
        df = get_data()
    if df is not None:
        submenu_choice = st.sidebar.selectbox("Subemnu", ["Descriptive", "Plots"])
        categorical_columns = df.select_dtypes(include=["object","category"]).columns.tolist()
        numerical_columns = df.select_dtypes(include=["number"]).columns.tolist()
        # fix column widths
        if len(categorical_columns) < 1:
            j= 0.1
        else:
            i = 1
        if len(numerical_columns) < 1:
            j = 0.1
        else: 
            j = 1
        if submenu_choice == "Descriptive":
            st.dataframe(df.head())
      

            c1, c2 = st.columns([i,j])
            with c1:
                with st.expander("Descriptive Statistics"):
                    if len(numerical_columns) >= 1:
                        selected_column = st.selectbox("Select a column", numerical_columns)
                        st.dataframe(df[selected_column].describe(), use_container_width=True)
            with c2:
                with st.expander("Categorical Distribution"):
                    if len(categorical_columns) >= 1:
                        selected_column = st.selectbox("Select a column", categorical_columns)
                        st.text(df[selected_column].value_counts())
        
        elif submenu_choice == "Plots":
            st.subheader("Plots")
            # Layouts
            col1,col2 = st.columns([i,j])
            
            with col1:
                with st.expander("Descriptive plots"):
                    if len(numerical_columns) >= 1:
                        selected_column = st.selectbox("Select a column", numerical_columns)                        
                        col_num = df[selected_column].nunique()
                        if col_num < 3:
                            tp_df = df[selected_column].value_counts().reset_index()
                            p1 = px.pie(tp_df, names=selected_column, values="count")
                            st.plotly_chart(p1, use_container_width=True)                            

                        else:
                            fig = px.histogram(df, x=selected_column)
                            st.plotly_chart(fig, use_container_width=True)
                            
                            st.subheader("Box Plot")
                            show_columns = [col for col in numerical_columns if df[col].nunique() < 3 and col != selected_column]
                            show_column = st.selectbox("Show Column", show_columns)
                            fig2 = px.box(df, x=selected_column, color= show_column)
                            st.plotly_chart(fig2, use_container_width=True)


            

            with col2:
                with st.expander("Categorical plots"):
                    column_list = df.select_dtypes(include=["object", "category"]).columns.tolist()
                    if len(column_list) >= 1:
                        selected_column = st.selectbox("Select a column", column_list)
                        tp_df = df[selected_column].value_counts().reset_index()
                        p1 = px.pie(tp_df, names=selected_column, values="count")
                        st.plotly_chart(p1, use_container_width=True)
            
            if len(numerical_columns) > 1:
                with st.expander("Correlation plots"):
                    numeric_df = df.select_dtypes(include = ['number'])
                    corr_matrix = numeric_df.corr()
                    fig = plt.figure(figsize=(20,10))
                    sns.heatmap(corr_matrix,annot=True)
                    #st.pyplot(fig)

                    p3 = px.imshow(corr_matrix)
                    st.plotly_chart(p3, use_container_width=True)


        


if __name__ == "__main__":
    run_eda_app()