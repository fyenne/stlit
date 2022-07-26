# Contents of ~/my_app/main_page.py
import pandas as pd
import streamlit as st
from datetime import datetime
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")





with st.form("input form"):
    message = st.text_input("user_name")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("Form checkbox")
    dt = datetime.now()
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        message = pd.Series([i.strip() for i in message.split(',')])
        # st.write("user" ,message)
        # st.write("slider", slider_val, "checkbox", checkbox_val)
        df = pd.DataFrame(
            {
                'message': message,
                'slider_val':slider_val,
                'checkbox_val': checkbox_val,
                'datetime': dt
            }, 
            index=range(len(message))).head(20)
        st.table(df)
        df.to_csv('./dataup/backup.csv', index = None, encoding = 'utf_8_sig')        

with st.form("query form"):
    submitted = st.form_submit_button("Submit")
    if submitted:
        df = pd.read_csv('./dataup/backup.csv')
        st.table(df)

