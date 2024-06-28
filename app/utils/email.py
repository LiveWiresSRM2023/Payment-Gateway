import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def send_email(recipient_email, subject, body):
    # Replace the following placeholders with your actual email credentials
    smtp_server = 'smtp.gmail.com'
    smtp_port = 587
    sender_email = 'your_email@gmail.com'
    sender_password = 'your_email_password'

    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = recipient_email
    message['Subject'] = subject
    message.attach(MIMEText(body, 'plain'))

    # Connect to the server and send the email
    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(sender_email, sender_password)
        text = message.as_string()
        server.sendmail(sender_email, recipient_email, text)
        server.quit()
        print('Email sent successfully')
    except Exception as e:
        print(f'Failed to send email: {e}')

def send_ticket_email(recipient_email, order_id, amount, customer_name):
    subject = 'Payment Successful'
    body = f'Dear {customer_name},\n\nYour payment of INR {amount} with Order ID {order_id} was successful.\n\nThank you for your purchase!'
    send_email(recipient_email, subject, body)
