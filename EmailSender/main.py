import smtplib
from email.mime.text import MIMEText

subject = "Test message"
body = """
Hello!

This is the body of the text message. 
Don't forget to subscribe to my channel!
"""
sender = "alina.chudnova@gmail.com"
recipients = ["a.chudnova.developer@gmail.com"] # you can add more receivers
password = "zwniczxwhmereluv"

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

send_email(subject, body, sender, recipients, password)