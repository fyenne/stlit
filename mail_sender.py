from datetime import datetime
import re
import smtplib
from email.mime.multipart import MIMEMultipart 


def sendEmailwithFile(account, server,receivers):
    """
    对每一行pd df_row 的循环. 
    """
    text = '''<p style="font-family:等线;font-size:10.5pt">Dear 
        <mark><b></b></mark> 
                '''

    subject = 'RE地产信息采集' 
    
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = account
    receivers = receivers
    msg['TO'] = receivers
    msg['Cc'] = ''
    text = msg.as_string()
    server.sendmail(account, receivers, text)
    # print('success')
    # server.quit()
    # time.sleep(2)
    
if __name__ == '__main__':
    server = smtplib.SMTP("smtp.163.com", 465)
    server.starttls()
    server.login('fyenneyenn@163.com', 'UOYKKXZLJLWMQWZL') # "zwfbctzjcynjymdh" #"17740821016@DI"
    sendEmailwithFile('fyenneyenn@163.com', server = server, receivers='fyenne@hotmail.com')
    server.quit()

