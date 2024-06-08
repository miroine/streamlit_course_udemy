import streamlit as st
import datetime
import sqlite3 
import timeago

conn = sqlite3.connect("data.db")
c = conn.cursor()

# Mgmt Fxn
def create_table():
    c.execute("CREATE TABLE IF NOT EXISTS chatstable(role TEXT,content TEXT, post_date DATE)")


def add_data(role,content,post_date):
    c.execute('INSERT INTO chatstable(role,content,post_date) VALUES (?,?,?)',(role,content,post_date))
    conn.commit()

# def view_all_chats():
#     c.execute("SELECT * FROM chatstable")
#     data = c.fetchall()
#     return data

def view_all_chats_as_dict():
    c.row_factory = sqlite3.Row
    c.execute("SELECT * FROM chatstable")
    data = c.fetchall()
    unpacked = [{k: item[k] for k in item.keys()} for item in data]
    return unpacked


def convert_time(date_string):
    #datetime_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f") # convert to proper datetime
    try:
        result = timeago.format(date_string - datetime.datetime.now())
    except TypeError:
        result = timeago.format(datetime.datetime.now() - datetime.datetime.now())
    return str(result).replace("in", "",1) # 1 is the first occurence

# def convert_time(date_string):
#     datetime_object = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f") # convert to proper datetime
#     result = timeago.format(datetime_object - datetime.datetime.now())
#     return str(result).replace("in", "",1) # 1 is the first occurence


# Init
create_table()

# Create a storage
if "messages" not in st.session_state:
    st.session_state.messages = view_all_chats_as_dict()

# Display chat history from database
# results = view_all_chats_as_dict()
# st.write(results)
# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message.get("role")):
        st.markdown(f'{message.get("content")} <sub>{convert_time(message.get("post_date",0))} ago</sub>',unsafe_allow_html=True)

sender = st.sidebar.selectbox("User", ["user","assistant"])        
prompt = st.chat_input("Send A Message")

if prompt:
    # Add to temporal storage
    st.session_state.messages.append({"role":sender,"content":prompt,"post_date": datetime.datetime.now()})

    # Add to persistant storage
    add_data(**{"role":sender,"content":prompt,"post_date": datetime.datetime.now()})
    # Display what was typed
    with st.chat_message('bot', avatar="😃"): # user
        st.write(prompt)