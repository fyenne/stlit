
# Contents of ~/my_app/pages/page_3.py
from email.policy import default
from aiohttp import Payload
from blinker import receiver_connected
import streamlit as st
from mail_sender import config
import re
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")



# add_plus = st.text_input('add a mail address')
# if add_plus is not None:
#     select_list = ["fyenne@hotmail.com"].append(add_plus)
#     st.write(select_list)
# else:
select_list = ["fyenne@hotmail.com"]

receiver = st.selectbox("to_whom", options = select_list)
content  = st.text_input('content')
file = st.file_uploader(label="file uploader", 
                        accept_multiple_files = True)



bt = st.button('send')
try:
    receiver = re.findall('\w+\@\w+\.\w+', receiver)[0]
    st.write('email format ok')
except:
    st.write('wrong')
    pass
if bt:
    a = config()
    print(receiver)
    a.run_(content = str(content), payload=file, receivers = str(receiver))
    # a.run_('aa', 'fyenne@hotmail.com')