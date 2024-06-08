import streamlit as st 


#Utils functions
import logging

#FORMAT 
LOGS_FORMAT = "%(levelname)s - %(asctime)s.%(msecs)03d - %(message)s"

# Create A logger 
logging.basicConfig(level=logging.DEBUG, format=LOGS_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
logger =logging.getLogger(__name__)

# save to file 
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

#formatter 
formatter = logging.Formatter(LOGS_FORMAT, datefmt="%Y-%m-%d %H:%M:%S")
# File 
file_handler = logging.FileHandler("activity.log")
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


def main():
    st.title("Adding logs to Application")
    st.text("Track all activities in the application")
    
    menu = ["Home", "EDA", "ML","About"]
    choice = st.sidebar.selectbox("Menu",menu) 
    
    if choice == "Home":
        st.subheader("Home")
        logger.info("Home Section")
    
    elif choice == "EDA":
        st.subheader("EDA Section")
        logger.info("EDA Section")
    
    elif choice == "ML":
        st.subheader("ML Section")
        logger.info("ML Section")
    
    elif choice == "Analytics":
        st.subheader("Analytics Section")
        logger.info("Analytics Section")
        
    else:
        st.subheader("About Section") 
        logger.info("About Section")
    
    
if __name__ == "__main__":
    main()
    