# No pip needed, built-in libraries
import csv
import smtplib
from email.mime.text import MIMEText

# Step 1: Create sample students.csv
with open('students.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Name', 'Email'])
    writer.writerow(['Ravi', 'ravi.test@example.com'])
    writer.writerow(['Teja', 'teja.test@example.com'])

# Step 2: Email Sending Code


sender_email = "your_email@gmail.com"
app_password = "your_16_digit_app_password"

with open('students.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        name = row['Name']
        receiver_email = row['Email']

        subject = f"Hello {name}, Project Update"
        body = f"Hi {name},\n\nThis is an automated email from Python.\nYour Python course is completed!\n\nRegards,\nPython Team"

        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender_email
        msg['To'] = receiver_email

        try:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
                server.login(sender_email, app_password)
                server.sendmail(sender_email, receiver_email, msg.as_string())
            print(f"Email sent to {name}")
        except Exception as e:
            print(f"Failed to send to {name}: {e}")