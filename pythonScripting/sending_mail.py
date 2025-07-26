import smtplib
from email.message import EmailMessage
from pathlib import Path
from string import Template

html = Template(Path('index.html').read_text())

email = EmailMessage()
email['from'] = 'sait-nac'
email['to'] = 'random@gmail.com'
email['subject'] = 'your random mail is not random anymore!'
email.set_content(html.substitute({'name': 'sof'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('sosofian849@gmail.com', '@')
    smtp.send_message(email)
    print('msg has ben sended')
