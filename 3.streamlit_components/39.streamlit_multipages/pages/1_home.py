import streamlit as st 

# sharing variables among pages 

from app import my_variable

st.subheader("Home Page")

st.write(my_variable)