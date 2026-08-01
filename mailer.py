from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import smtplib
from dotenv import load_dotenv
import os

load_dotenv()
gmail_address = ("GMAIL_ADDRESS")
gmail_app_password = ("GMAIL_APP_PASSWORD")


def send_email (subject, body):
   msg = MIMEMultipart()
   msg["subject"] = subject
   msg["From"] = gmail_address
   msg["To"] = gmail_address

   MIMEText(body, "plain")
   msg.attach(MIMEText)

   server = smtplib.SMTP("stmp.gmail.com", 587)
   server.starttls()
   server.login(gmail_address, gmail_app_password)
   server.send_message(msg)
   server.quit()


if __name__ == "__main__":
   send_email("test Email", "This is a test from my python script")
   

