# config.py : where I keep my keys as constants
import config
import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dominik Korpusik'
email['to'] = config.TO_EMAIL
email['subject'] = 'You won a 1,000,000 dollrs!'

email.set_content(html.substitute({'name': 'TinTin', 'age': 20}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    email_address = config.EMAIL_ADDRESS
    email_pass = config.EMAIL_PASSWORD
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_address, email_pass)
    smtp.send_message(email)
