class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'  # Or your production DB URI
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your-secret-key'
