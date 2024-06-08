import streamlit as st 
import datetime

# create storage for chat history 

if "messages" not in st.session_state:
    st.session_state["messages"] = []

#Display the chat history 
st.write(st.session_state["messages"])

for messages in st.session_state.messages:
    with st.chat_message(messages["role"]):
        st.write(messages["content"])
        st.write(messages["post_date"])

prompt = st.chat_input("Ask something")

# Display the messages 
if prompt:
    # add the user prompt to chat history 
    st.session_state["messages"].append({"role":"user",
                                         "content":prompt, "post_date":datetime.datetime.now()})
    # Display the chat history 
    #st.session_state["messages"].append({"role":"bot", "content":prompt, "post_date":datetime.datetime.now()})
    with st.chat_message("user"):
        st.write(prompt)
    
