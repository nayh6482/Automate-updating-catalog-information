#!/usr/bin/env python3

import os, datetime , reports,emails

# title

from datetime import datetime

now = datetime.now()
formatted_date = now.strftime("%B %d")
title = f"Processed Update on {formatted_date}"

# formatting the paragraph
path = "supplier-data/descriptions/"
paragraph = ""
for file in os.listdir("supplier-data/descriptions/"):
    with open(path + file, "r") as f:
        content = f.read()
        fruit_value_list = content.splitlines()
        fruit_name = fruit_value_list[0].strip()
        fruit_weight = int(fruit_value_list[1].strip().split()[0])
        fruit_description = fruit_value_list[2].strip()
        paragraph += f"name: {fruit_name}<br/>weight: {fruit_weight} lbs<br/><br/>"

if __name__ == "__main__":
      reports.generate_report("/tmp/processed.pdf", title, paragraph)

      #send email
      sender = "automation@example.com"
      recipient = "{}@example.com".format(os.environ["USER"])
      subject = "Upload Completed - Online Fruit Store"
      body = "All fruits are uploaded to our website successfully. A detailed list is attached to this email."
      attachment = "/tmp/processed.pdf"
      message = emails.generate_email(sender, recipient, subject, body, attachment)
      emails.send_email(message)
