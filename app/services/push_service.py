import requests

def send_push_notification(notification):
    user = User.query.get(notification.user_id)
    content = Content.query.get(notification.content_id)

    payload = {
        'to': user.device_token,  # Assuming each user has a device token
        'notification': {
            'title': f"New Content: {content.title}",
            'body': content.description,
            'click_action': content.link
        }
    }
    
    # Push service endpoint (e.g., Firebase Cloud Messaging)
    response = requests.post('https://fcm.googleapis.com/fcm/send', json=payload, headers={'Authorization': 'key=your-fcm-key'})
    print(response.status_code, response.text)
