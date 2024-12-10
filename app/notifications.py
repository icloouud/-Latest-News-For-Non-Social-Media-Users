from app.models import NotificationQueue
from app.services.email_service import send_email
from app.services.push_service import send_push_notification
from app.services.sms_service import send_sms

def queue_notifications():
    notifications = NotificationQueue.query.filter_by(sent=False).all()
    for notification in notifications:
        if notification.notification_type == 'email':
            send_email(notification)
        elif notification.notification_type == 'push':
            send_push_notification(notification)
        elif notification.notification_type == 'sms':
            send_sms(notification)
        
        notification.sent = True
        db.session.commit()
