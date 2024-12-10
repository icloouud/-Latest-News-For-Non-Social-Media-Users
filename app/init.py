# Initialize the app and set up the database and configurations
from flask import Flask
from app.models import db
from app.services.email_service import send_email
from app.services.push_service import send_push_notification
from app.services.sms_service import send_sms

def create_app():
    app = Flask(__name__)
    
    # Configuration
    app.config.from_object('config.config.Config')
    
    # Initialize the database
    db.init_app(app)
    
    return app
app/init.py
