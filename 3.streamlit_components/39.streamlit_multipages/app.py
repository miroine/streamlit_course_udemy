import streamlit as st 


my_variable = "From Main App.py Page"
def main():
    st.subheader ("Streamlit Multi App")
    st.title("Main Page")
    st.write(my_variable)
    


if __name__ == "__main__":
    main()