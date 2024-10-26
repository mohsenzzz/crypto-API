
import smtplib

from email.mime.text import MIMEText
from local_config import EMAIL_PASSWORD

def send_smtp_mail(subject, body):
    """
    get subject and body and send email
    """
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = '229f931d15-6adb42@inbox.mailtrap.io'
    msg['To'] = 'mohsenzarei291@gmail.com'

    with smtplib.SMTP('live.smtp.mailtrap.io', 587) as server:
        server.login('smtp@mailtrap.io', EMAIL_PASSWORD)
        server.sendmail(msg['From'], msg['To'], msg.as_string())


