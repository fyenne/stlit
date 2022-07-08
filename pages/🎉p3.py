
# Contents of ~/my_app/pages/page_3.py
from blinker import receiver_connected
import streamlit as st
from mail_sender import config
import re
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")



receiver = st.selectbox("to_whom", options = ["fyenne@hotmail.com"])
content  = st.text_input('content')
bt = st.button('send')

try:
    receiver = re.findall('\w+\@\w+\.\w+', receiver)[0]
    st.write('ok')
except:
    st.write('wrong')
    pass
if bt:
    a = config()
    print(receiver)
    a.run_(str(content), str(receiver))
    # a.run_('aa', 'fyenne@hotmail.com')