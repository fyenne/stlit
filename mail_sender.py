from datetime import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase
from email import encoders


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
        # with open(attachment, 'rb') as fp:
        # img = MIMEImage(file)
        # img.add_header('Content-ID', '<{}>'.format('a pic'))
        # msg.attach(img)
        output_name1 = 'name'
        part1 = MIMEBase('application', "octet-stream")
        part1.set_payload(payload)
        encoders.encode_base64(part1)
        part1.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', output_name1))
        msg.attach(part1)

        # ============================================================================ #
        #                                    config                                    #
        # ============================================================================ #
        msg['From'] = account
        receivers = receivers
        msg['TO'] = receivers
        msg['Cc'] = ''
        text = msg.as_string()
        server.sendmail(account, receivers, text)
        
        
    def run_(self, content , payload, receivers):        
        self.server.starttls()
        self.server.login(self.mail, self.pw)
        print('connecting...')
        try:
            self.sendEmailwithFile(self.mail, server = self.server, content = content, payload=payload, receivers=receivers)
            print("SUCCESS")
        except Exception as e:
            raise ValueError(e)
        self.server.quit()

