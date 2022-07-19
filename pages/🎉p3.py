
# Contents of ~/my_app/pages/page_3.py
from email.policy import default
from aiohttp import Payload
from blinker import receiver_connected
import streamlit as st
from mail_sender import config
import re
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")



add_plus = st.text_input('add a mail address')
if add_plus is not None:
    select_list = ["fyenne@hotmail.com"]+ [str(add_plus)]
else:
    select_list = ["fyenne@hotmail.com"]
receiver = st.multiselect("to_whom", options = select_list, default = 'fyenne@hotmail.com')
st.write(select_list)

# try:
#     receiver = re.findall('\w+\@\w+\.\w+', receiver)[0]
#     st.write('email format ok')
# except:
#     st.write('wrong')
#     pass
# ============================================================================ #
#                                 send_content                                 #
# ============================================================================ #
st.markdown('---')

content  = st.text_input('content')
file = st.file_uploader(label="file uploader", 
                        accept_multiple_files = True)



bt = st.button('send')

if bt:
    a = config()
    print(receiver)
    res = a.run_(content = str(content), payload=file, receivers = receiver)
    # a.run_("content", payload=None, receivers = 'fyenne@hotmail.com')
    while res is None:
        with st.spinner('Wait for it...'):
            pass
    
    st.markdown('**succeed mail**') 