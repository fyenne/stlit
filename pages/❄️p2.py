# Contents of ~/my_app/main_page.py
import pandas as pd
import numpy as np
import streamlit as st
from datetime import datetime
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")





with st.form("input form"):
    message = st.text_input("user_name")
    slider_val = st.slider("Form slider")
    checkbox_val = st.checkbox("append dataframe?")
    dt = str(datetime.now())
    
    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")
    if submitted:
        message = pd.Series([i.strip() for i in message.split(',')])
        
        df = pd.DataFrame(
                {
                    'message': message,
                    'slider_val':slider_val,
                    'checkbox_val': checkbox_val,
                    'datetime': dt
                }, 
                index=range(len(message))).head(20)
        if checkbox_val == True:
            # st.write('true')
            appender = pd.read_csv('./dataup/backup.csv')
            df = appender.append(df)
        else:
            pass
        st.table(df)
        df.to_csv('./dataup/backup.csv', index = None, encoding = 'utf_8_sig')

with st.container():
    with st.form("query form"):
        submitted = st.form_submit_button("show history")
        if submitted:
            df = pd.read_csv('./dataup/backup.csv')
            st.table(df)
            
        
with st.container():
    bt = st.button("truncate table?")
    if bt:
        st.balloons()
        pd.DataFrame({
                    'message': 'message',
                    'slider_val':'slider_val',
                    'checkbox_val': 'checkbox_val',
                    'datetime': dt
                }, 
                index=range(1)).\
            to_csv('./dataup/backup.csv', index = None, encoding = 'utf_8_sig')
        
