import streamlit as st 

#Load EDA packages 
import pandas as pd 
import numpy as np

#load data viz pkg 
import matplotlib.pyplot as plt 
import seaborn as sns 
import plotly.express as px 
import plotly.graph_objects as go 
import plotly.figure_factory as ff 
import plotly.io as pio
import altair as alt 

def main():
    st.title("Plotting with st.Pyplot")
    df = pd.read_csv("Iris.csv")
    st.dataframe(df.head())
    #col1 ,padding, col2 = st.columns((10,2,10))
    col1, col2 = st.columns(2, gap="large")
    with col1:
        #matplotlib
        fig, ax = plt.subplots()
        ax.scatter(*np.random.random(size=(2, 1000)))   
        st.pyplot(fig)
    
    with col2:
        # use seaborn
        fig = plt.figure() 
        sns.countplot(x="Species", data=df)
        st.pyplot(fig)
    
    st.divider()
    
    # using bar_chart 
    st.bar_chart(df.loc[:,['SepalLengthCm' ,'PetalLengthCm']])

    #Line chart
    vector = df.columns [df.columns.str.contains("Cm")].tolist()
    lang_choices = st.multiselect("Choose vector", vector) 
    col1, gap,col2 = st.columns((10,1,10))
    with col1:
        st.line_chart(df.loc[:,lang_choices]) 
    with col2:
        st.area_chart(df.loc[:,lang_choices])
        
    
    st.divider()
    
    # plotting with Altair 
    df = pd.DataFrame(
        np.random.randn(100, 3),
        columns=['a', 'b', 'c']
    )
    col1 = st.container()
    with col1:
        c = alt.Chart(df).mark_circle().encode(
            x='a',
            y='b',
            size='c',
            color='c', tooltip=['a', 'b', 'c'])
        
        st.dataframe(df.head(), use_container_width=True)
        
        st.altair_chart(c, use_container_width=True)
   
        

if __name__ == "__main__":
    main()