from app.models import db, Content, User, NotificationQueue
from datetime import datetime

def add_new_content(title, content_type, link, description):
    # Create a new content object
    new_content = Content(
        title=title,
        content_type=content_type,
        link=link,
        description=description,
        release_date=datetime.utcnow()
    )
    
    # Save to database
    db.session.add(new_content)
    db.session.commit()

    # Trigger notifications
    send_notifications(new_content)

def send_notifications(content):
    # Find users who want notifications for this content type
    users = User.query.filter(User.preferences.contains({content.content_type})).all()
    for user in users:
        notification = NotificationQueue(user_id=user.id, content_id=content.id, notification_type='push')
        db.session.add(notification)
    
    db.session.commit()
    # Call function to send notifications to users
    queue_notifications()
