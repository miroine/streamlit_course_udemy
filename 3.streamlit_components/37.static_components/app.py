import streamlit as st 

# components
import streamlit.components.v1 as stc


def main():
    st.title("Streamlit static components")
    
    stc.html("<p style='color:red;'>Streamlit is Awesome </p>")
    st.markdown("<p style='color:blue;'>Streamlit is Awesome </p>",
                unsafe_allow_html=True)
    
    st.text("From W3Schools")
    HtmlFile = open("test.html","r")
    source_code = HtmlFile.read()
    stc.html(source_code, height=200)
    
    st.text("From iframe")
    stc.iframe("https://www.google.com/webhp?igu=1", 
               height=300, scrolling=True)

if __name__ == "__main__":
    main()