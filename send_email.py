'''
A simple script to send email to single or multiple person.
Usage:
1. Download the script and manually provide the login credential and allow less secure app in your gmail (or Google Account) security settings.
2. Run this script using interactive shell or cmd like: python -i send_email.py. You will get interactive python shell.
3. Exectue this function as command: send_email(from_email='your email id', to_emails=['receiver's email id'], msg_body='Email Body', subject='Testing',html=None)
4. Provide some positional arguments like form (string), to (string or list of string), msg_body (string), subject (string), and optional html msg.
5. Hit enter to run the script.

You will get the automated version of th emanual part of this script sometime later.
'''

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


username = 'something@gmail.com'
password = 'somebody@123'

def send_email(msg_body='Email Body', subject='Testing',from_email='ishversoni16@gmail.com', to_emails=None, html=None):
    assert isinstance(to_emails, list)

# formulating the message
    msg = MIMEMultipart('alternative')
    msg['From'] = from_email
    msg['To'] = ', '.join(to_emails)
    msg['Subject'] = subject
    
    text_msg = MIMEText(msg_body, 'plain')
    msg.attach(text_msg)

    if html != None:    
        html_msg = MIMEText(f'<h1>{html}</h1>', 'html')
        msg.attach(html_msg)

    msg_string = msg.as_string()

    #login to my smtp server
    server = smtplib.SMTP(host='smtp.gmail.com', port=587)  # connecting to gmail smtp server
    server.ehlo()           # some default configuration
    server.starttls()       # starting secure layer
    server.login(username, password) # login
    server.sendmail(from_email, to_emails, msg_string)
    server.quit()

    

'''
with smtplib.SMTP() as server:
    pass
'''