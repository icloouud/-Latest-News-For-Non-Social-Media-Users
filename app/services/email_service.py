import smtplib
from email.mime.text import MIMEText
from app.models import User, Content

def send_email(notification):
    user = User.query.get(notification.user_id)
    content = Content.query.get(notification.content_id)
    
    subject = f"New Content Available: {content.title}"
    body = f"Hi {user.name},\n\nCheck out the new content: {content.title}\n\n{content.description}\n\nLink: {content.link}"
    
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@example.com'
    msg['To'] = user.email

    with smtplib.SMTP('smtp.example.com') as server:
        server.sendmail(msg['From'], [msg['To']], msg.as_string())
