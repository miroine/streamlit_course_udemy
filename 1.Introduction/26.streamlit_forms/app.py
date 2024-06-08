import streamlit as st 
import pandas as pd 


def main():
    st.title("Streamlit App Forms & Salary Calculator")
    menu = ["Home", "About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Forms tutorial")
    
    # salary calculation
    
    
        with st.form(key="salary_form"):
            col1, col2, col3 = st.columns([3,2,1])
            #method 1: Context manager approach (with)
            with col1:
                amount = st.number_input("Rate in $")
            with col2:
                hours_per_week = st.number_input("Hours Per Week", 1,120)
            with col3:
                st.text("Salary")
                submit_salary= st.form_submit_button(label="Calculate")
            
            if submit_salary:
                with st.expander("Salary Calculator"):
                    daily = [amount * 8]
                    weekly = [amount * hours_per_week]
                    salary = [daily * 260]
                    df = pd.DataFrame({"hourly":amount, "daily":daily, "salary":weekly})
                    st.dataframe(df.T) 
                    
        
        with st.form(key="form1"):
            firstname = st.text_input("First Name")
            lastname = st.text_input("Last Name")
            dob = st.date_input("Date of Birth")
            
            submit_button = st.form_submit_button(label="SignUp")
        
        if submit_button:
            st.success(f"Welcome {firstname} {lastname}")
            st.info(f"Your DOB is {dob}")
        
        # Method 2: Variable approach 
        form2 = st.form(key="form2")
        username = form2.text_input("Username")
        jobtype = form2.selectbox("Job Type",["Data Analyst", "Data Scientist"])
        password = form2.text_input("Password",type="password")
        submit_button2 = form2.form_submit_button(label="SignUp")
        if submit_button2:
            st.success(f"Welcome {username}")
            st.info(f"Your Job Type is {jobtype}")
            st.info(f"Your Password is {password}")
    
    else:
        st.subheader("About")

    


if __name__ == "__main__":
    main()