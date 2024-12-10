from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Content(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content_type = db.Column(db.String(50), nullable=False)  # Article, Podcast, Video
    link = db.Column(db.String(255), nullable=False)
    description = db.Column(db.String(500), nullable=True)
    release_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f'<Content {self.title}>'

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False, unique=True)
    phone = db.Column(db.String(20), nullable=True)
    preferences = db.Column(db.JSON, nullable=False)  # Store preferences as JSON (e.g., { "content_type": ["podcast", "video"] })

    def __repr__(self):
        return f'<User {self.name}>'

class NotificationQueue(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    content_id = db.Column(db.Integer, db.ForeignKey('content.id'), nullable=False)
    notification_type = db.Column(db.String(50))  # push, email, sms
    sent = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f'<NotificationQueue User {self.user_id} Content {self.content_id}>'
