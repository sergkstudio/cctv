from flask import request, jsonify
from app import app, db
from models import User, Video
from flask_jwt_extended import create_access_token, jwt_required

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

@app.route('/videos', methods=['GET'])
@jwt_required()
def get_videos():
    videos = Video.query.all()
    return jsonify([{"id": v.id, "camera_id": v.camera_id, "start_time": v.start_time, "end_time": v.end_time, "file_path": v.file_path} for v in videos])
