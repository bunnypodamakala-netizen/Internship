import csv
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Email sender details
sender_email = os.getenv("SENDER_EMAIL")
sender_password = os.getenv("SENDER_APP_PASSWORD")


# Dynamic subject and message
subject = "Important Student Information"


def send_email(receiver_email, student_name):
    message = MIMEMultipart()

    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    body = f"""
Hello {student_name},

This is a personalized message for you.

Please check the latest student information.

Thank you,
Student Management Team
"""

    message.attach(MIMEText(body, "plain"))

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())

    print("Email sent to:", student_name)


# Read CSV file
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)

    for student in reader:
        send_email(student["Email"], student["Name"])

print("All emails processed successfully!")
