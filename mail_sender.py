from datetime import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 



class config():
    def __init__(self):
        self.server = smtplib.SMTP("smtp.office365.com", 587)
        self.mail = 'fyenneyenn@hotmail.com'
        self.pw = 'NOmoreuse7-'
    
    def sendEmailwithFile(self, account, server, content, receivers):
        """
        对每一行pd df_row 的循环. 
        """
        text = '''<p style="font-family:等线;font-size:10.5pt">memo: 
            <mark><b>mooo</b></mark><br />
                    '''
        text = text + content
        subject = 'message__' + str(datetime.now()) 
        
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg.attach(MIMEText(text, 'html', 'utf-8'))

        msg['From'] = account
        receivers = receivers
        msg['TO'] = receivers
        msg['Cc'] = ''
        text = msg.as_string()
        server.sendmail(account, receivers, text)
        
        
    def run_(self, content , receivers):        
        self.server.starttls()
        self.server.login(self.mail, self.pw)
        print('connecting...')
        try:
            self.sendEmailwithFile(self.mail, server = self.server, content = content, receivers=receivers)
            print("SUCCESS")
        except Exception as e:
            raise ValueError(e)
        self.server.quit()

