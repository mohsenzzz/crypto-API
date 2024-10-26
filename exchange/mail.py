
import smtplib

from email.mime.text import MIMEText

def send_mail(subject, body):
    """
    get subject and body and send email
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = '<EMAIL>'
    msg['To'] = '<EMAIL>'

    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.login('<EMAIL>', 'password')
        server.sendmail('<EMAIL>', '<EMAIL>', msg.as_string())


