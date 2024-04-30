from flask import Flask, render_template, request
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        subject = request.form['subject']
        message = request.form['message']

        # Send email
        send_email(name, email, subject, message)

        # Render success message inline
        return f"<h1>Success!</h1><p>Your message has been sent. Thank you!</p>"
    else:
        return render_template('index.html')

def send_email(name, email, subject, message):
    # Your SMTP server configuration
    smtp_server = 'smtp.example.com'
    smtp_port = 587  # Change this if your SMTP server uses a different port
    smtp_username = 'your_smtp_username'
    smtp_password = 'your_smtp_password'

    # Create message container
    msg = MIMEMultipart()
    msg['From'] = email
    msg['To'] = 'recipient@example.com'  # Change this to the recipient's email address
    msg['Subject'] = subject

    # Add message body
    body = f"Name: {name}\nEmail: {email}\n\n{message}"
    msg.attach(MIMEText(body, 'plain'))

    # Connect to SMTP server and send email
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.send_message(msg)

if __name__ == '__main__':
    app.run(debug=True)


