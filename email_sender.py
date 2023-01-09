import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Dominik Korpusik'
email['to'] = 'dominik.korpusik@gmail.com'
email['subject'] = 'You won a 1,000,000 dollrs!'

email.set_content(html.substitute({'name': 'TinTin', 'age': 20}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    email_address = 'kowalczykaa37@gmail.com'
    email_pass = 'ajxavpjeaxnoflyc'
    smtp.ehlo()
    smtp.starttls()
    smtp.login(email_address, email_pass)
    smtp.send_message(email)
    print("All good boss!")