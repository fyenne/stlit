# Contents of ~/my_app/main_page.py
import pandas as pd
import streamlit as st
import time
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")





with st.form("my_form"):
    message = st.text_input("user_name")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        st.write("user" ,message)
        st.write("slider", slider_val, "checkbox", checkbox_val)
        pd.DataFrame({'message': message, 'slider_val':slider_val, 'checkbox_val': checkbox_val}, index=range(1)).to_csv('./dataup/backup.csv')        
    # with st.spinner('Wait for it...'):
