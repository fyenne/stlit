
# Contents of ~/my_app/pages/page_3.py
from email.policy import default
from aiohttp import Payload
from blinker import receiver_connected
import streamlit as st
from mail_sender import config
import re
st.markdown("# Page 3 🎉")
st.sidebar.markdown("# Page 3 🎉")



def save_uploadedfile(uploadedfile):
    with open(os.path.join(tmp_dir,uploadedfile.name),"wb") as f:
        f.write(uploadedfile.getbuffer())
    return st.success("Saved File:{} to tempDir".format(uploadedfile.name))



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
files = st.file_uploader(label="file uploader", 
                        accept_multiple_files = True)
if files != None:    
    # st.write(file.name)
    for file in files:
        file_details = {"filename":file.name, 
                        "filetype":file.type,
                        "filesize":file.size}
        st.write(file_details)
# ---
bt = st.button('send')


res = None 
if bt:
    # ============================================================================ #
    #                       create file path for tmp storage                       #
    # ============================================================================ #
    import os
    import time
    tmp_dir = './tmp_files/' 
    try:
        os.mkdir(tmp_dir)
    except:
        pass
    for file in files:
        save_uploadedfile(file)
    
    # ============================================================================ #
    a = config()
    res = a.run_(content = str(content), payload=(tmp_dir+file.name), receivers = receiver)

    
    st.markdown('**succeed mail**') 
    while a == 0:
        with st.spinner('Wait for it...'):
            time.sleep(1)
            del a
    try:
        import shutil
        shutil.rmtree('./tmp_files/')
    except:
        pass