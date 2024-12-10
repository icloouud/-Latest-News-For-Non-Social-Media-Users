from twilio.rest import Client

def send_sms(notification):
    user = User.query.get(notification.user_id)
    content = Content.query.get(notification.content_id)
    
    # Twilio configuration (replace with actual credentials)
    client = Client('ACCOUNT_SID', 'AUTH_TOKEN')
    
    message = client.messages.create(
        body=f"New Content Available: {content.title}. Check it out: {content.link}",
        from_='+1234567890',  # Your Twilio phone number
        to=user.phone
    )
