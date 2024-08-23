from backend.app_old import db
from datetime import datetime

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(50), nullable=False)  # роли: 'admin', 'viewer'

class Video(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    camera_id = db.Column(db.String(80), nullable=False)
    start_time = db.Column(db.DateTime, nullable=False)
    end_time = db.Column(db.DateTime, nullable=False)
    file_path = db.Column(db.String(120), nullable=False)

class SharedStream(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    stream_url = db.Column(db.String(120), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    expires_at = db.Column(db.DateTime, nullable=False)
