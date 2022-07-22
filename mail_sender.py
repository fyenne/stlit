from datetime import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders
from typing import List
import streamlit as st

class config():
    def __init__(self):
        self.server = smtplib.SMTP("smtp.office365.com", 587)
        self.mail = 'fyenneyenn@hotmail.com'
        self.pw = 'NOmoreuse7-'
    
    def sendEmailwithFile(self, account, server, content, payload, receivers):
        """
        对每一行pd df_row 的循环. 
        """
        msg = MIMEMultipart()
        subject = 'message__' + str(datetime.now()) 
        msg['Subject'] = subject
        
        # ============================================================================ #
        #                                      txt                                     #
        # ============================================================================ #
        text = '''<p style="font-family:等线;font-size:10.5pt">memo: 
            <mark><b>mooo</b></mark><br />
                    '''
        text = text + content
        msg.attach(MIMEText(text, 'html', 'utf-8'))
        
        # ============================================================================ #
        #                                      file                                    #
        # ============================================================================ #
        # output_name1 = 'name'
        def name_mutate(name):
            return re.findall('(?<=\/)\w+\.\w+', str(name))
        
        def attach_file(payload):    
            part1 = MIMEBase('application', "octet-stream") 
            part1.set_payload(open(payload, "rb").read())
            encoders.encode_base64(part1) 
            # try:
            #     st.write(re.findall('\.\w+', payload), 'format of file')
            # except:
            #     st.write(re.findall('?>=\.\w+', payload))
            #     st.write(re.findall('\w+(?=\.\w+)', payload))
            #     pass 
            part1.add_header(
                'Content-Disposition',
                'attachment', 
                filename=('utf-8', '',  name_mutate(payload)[0]))
            msg.attach(part1)
            
        if payload is List:
            payloads = payload
            for payload in payloads:
                attach_file(payload)
        else:
            attach_file(payload)

        # ============================================================================ #
        #                                    config                                    #
        # ============================================================================ #
        msg['From'] = account
        receivers = receivers
        msg['TO'] = receivers
        msg['Cc'] = ''
        text = msg.as_string()
        server.sendmail(account, receivers, text)
        
        
    def run_(self, content, payload, receivers):        
        self.server.starttls()
        self.server.login(self.mail, self.pw)
        st.write('connecting...')
        try:
            print(
                """
                # ============================================================================ #
                # ============================================================================ #
                """
                ,type(receivers)
                
            )
            if type(receivers) is list:
                for i in receivers:    
                    self.sendEmailwithFile(
                        account= self.mail,
                        server = self.server,
                        content = content,
                        payload=payload,
                        receivers=i)
                    st.write("SUCCESS to address", i)
                pass
            
            elif type(receivers) is str:
                self.sendEmailwithFile(
                    self.mail,
                    server = self.server,
                    content = content,
                    payload=payload,
                    receivers=receivers)
                st.write("SUCCESS", receivers)
            else:
                raise Exception("eeeeemmmmmmmmmmm")
        except Exception as e:
            raise ValueError(e)
        self.server.quit()
        return 0



# a = config()
# server = smtplib.SMTP("smtp.office365.com", 587)
# server.starttls()
# server.login(a.mail,a.pw)
# content = ''
# payload = r"C:\Users\dscshap3808\Documents\fapiao\202109.pdf"
# a.sendEmailwithFile(account=a.mail, server=server, content=content, payload=payload, 
#                     receivers='siming.yan@sf-dsc.com')
# server.quit() 
# q(?=u) matches a q that is followed by a u,
# (?<=a)b (positive lookbehind) matches the b (and only the b) in cab, 


