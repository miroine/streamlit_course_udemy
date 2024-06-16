# Core Pkgs 
import streamlit as st 
import streamlit.components.v1 as stc


# EDA Pkgs 
import pandas as pd
import numpy as np

#plotting
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib
import plotly.express as px

matplotlib.use("agg")
#utils fcts
from  db_function import *
def main():
    st.title("ToDo App with Streamlit application")
    
    menu = ["Create", "Read", "Update", "Delete", "About"]
    choice = st.sidebar.selectbox("Menu", menu)
    
    create_table()
    if choice == "Create":
        st.subheader("Add Iterms")
        
        #Layout 
        col1, col2 = st.columns(2)
        
        with col1:
            item = st.text_area("Enter Item")
        with col2:
            task_status = st.selectbox("Status", ["ToDo","Doing","Done"])
            task_due_date = st.date_input("Due Date")
            if st.button("Add Item"):
                add_data(item, task_status, task_due_date)
                st.success(f"successfully added {item}")
    
    elif choice == "Read":
        st.subheader("View Iterms")
        data = view_all_data()
        #st.write(data)
        df = pd.DataFrame(data, columns=['tasks','status','tasks_due_date'])
        with st.expander("View all data"):            
            st.dataframe(df)
        
        with st.expander("Task Status"):
            task_df = df['status'].value_counts()
            st.bar_chart(task_df)
            p1 = px.pie(task_df.reset_index() , values='count', names='status')
            st.plotly_chart(p1)
            
        
    elif choice == "Update":
        st.subheader("Edit/Update Iterms")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['tasks','status','tasks_due_date'])
        with st.expander("Current data"):
            st.dataframe(df)

        list_of_tasks = [i[0] for i in view_unique_task()]
        task_to_update = st.selectbox("Select task to update", list_of_tasks)
        
        selected_results = get_task(task_to_update)
        st.write(selected_results)
        
        if selected_results:
            task = selected_results[0][0]
            task_status = selected_results[0][1]
            task_due_date = selected_results[0][2]
            
            col1 , col2 = st.columns(2)
            with col1:
                new_task = st.text_area("task to Do",task)
            with col2:
                new_task_status = st.selectbox(task_status, ["ToDo","Doing","Done"])
                new_task_due_date = st.date_input(task_due_date)
            if st.button("Update"):
                update_task(new_task, new_task_status, new_task_due_date, task, task_status, task_due_date)
                st.success(f"successfully updated {new_task}")
        
                result = view_all_data()
                df = pd.DataFrame(result, columns=['tasks','status','tasks_due_date'])
                with st.expander("Updated data"):
                    st.dataframe(df)
    
    elif choice == "Delete":
        st.subheader("Delete Iterms")
        result = view_all_data()
        df = pd.DataFrame(result, columns=['tasks','status','tasks_due_date'])
        with st.expander("Current data"):
            st.dataframe(df)
        list_of_tasks = [i[0] for i in view_unique_task()]
        task_to_update = st.selectbox("Select task to update", list_of_tasks)
        selected_results = get_task(task_to_update)
        st.write(selected_results)
        
        if selected_results:
            task = selected_results[0][0]
            task_status = selected_results[0][1]
            task_due_date = selected_results[0][2]
        st.warning(f"Are you sure you want to delete {task}")
        if st.button("Delete"):          
            delete_task(task, task_status, task_due_date)
            st.success(f"successfully deleted {task}")
            result = view_all_data()
            df = pd.DataFrame(result, columns=['tasks','status','tasks_due_date'])
            with st.expander("Updated data"):
                st.dataframe(df)
        
    
    else:
        st.subheader("About")
        



if __name__ == '__main__':
    main()