# Load EDA pkgs
import streamlit as st
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd 


def run_eda_app():
    st.subheader("From Explorotary Data Analysis")
    df = pd.read_csv("./data/diabetes.csv")
    st.dataframe(df) 