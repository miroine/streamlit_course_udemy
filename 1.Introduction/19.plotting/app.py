import streamlit as st 
import pandas as pd 
import numpy as np 
import math



# load data Vis Pkg 
import plotly.express as px 


def _generate_dataframe (size=100) -> dataframe : 
 
import streamlit as st 
import pandas as pd 
import numpy as np 
import math

# load data Vis Pkg 
import plotly.express as px 

def _generate_dataframe(size=100):
    x = pd.Series(np.random.rand(size))
    y = x ** 2 + 2 * x + 4
    df = pd.DataFrame({"x": x, "y": y})
    return df 

def main():
    """
    This function is the main entry point of the Streamlit application.
    It sets up the title, generates a dataframe, and creates a scatter plot using Plotly.

    Parameters:
    None

    Returns:
    None
    """
    st.title("plotting in Streamlit with plotly")  # Set the title of the application

    df = _generate_dataframe()  # Generate a dataframe using the _generate_dataframe function
    st.dataframe(df)  # Display the dataframe in the Streamlit application

    fig = px.scatter(data_frame=df, x="x", y="y")  # Create a scatter plot using Plotly
    st.plotly_chart(fig)  # Display the scatter plot in the Streamlit application
    
# TODO: implementation 
#! important feature 

if __name__ == "__main__":
    main()
    y = x **2 + 2* x +4
    df = pd.DataFrame({"x":x, "y":y})
    return df 
def main():
    """
    This function is the main entry point of the Streamlit application.
    It sets up the title, generates a dataframe, and creates a scatter plot using Plotly.

    Parameters:
    None

    Returns:
    None
    """
    st.title("plotting in Streamlit with plotly")  # Set the title of the application

    df = _generate_dataframe()  # Generate a dataframe using the _generate_dataframe function
    st.dataframe(df)  # Display the dataframe in the Streamlit application

    fig = px.scatter(data_frame=df, x="x", y="y")  # Create a scatter plot using Plotly
    st.plotly_chart(fig)  # Display the scatter plot in the Streamlit application
    
# TODO: implementation 
# ! important feature 

if __name__ == "__main__":
    main()