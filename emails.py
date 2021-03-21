#!/usr/bin/env python3

import smtplib
from email.message import EmailMessage
import os.path
import mimetypes

def generate_email(sender, recipient, subject, body, attachment=None):
    message = EmailMessage()
    message['Subject'] = subject
    message['From'] = sender
    message['To'] = recipient
    message.set_content(body)
    if attachment != None:
        attachment_path = attachment
        attachment_filename = os.path.basename(attachment_path)
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split("/", 1)
        with open(attachment_path, 'rb') as ap:
            message.add_attachment(ap.read(),
                                    maintype=mime_type,
                                    subtype=mime_subtype,
                                    filename=os.path.basename(attachment_path))
    return message

def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
