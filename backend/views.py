from flask import request, jsonify, send_file, url_for
from backend.app_old import app, db
from backend.models_old import User, Video, SharedStream
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from datetime import datetime, timedelta
import os

# Регистрация пользователя
@app.route('/register', methods=['POST'])
@jwt_required()
def register():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({"msg": "Admin access required"}), 403
    
    data = request.json
    new_user = User(username=data['username'], password=data['password'], role=data['role'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created"}), 201

# Аутентификация пользователя
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = User.query.filter_by(username=data['username']).first()
    if user and user.password == data['password']:
        access_token = create_access_token(identity={'username': user.username, 'role': user.role})
        return jsonify(access_token=access_token), 200
    return jsonify({"msg": "Invalid credentials"}), 401

# Получение видеозаписей
@app.route('/videos', methods=['GET'])
@jwt_required()
def get_videos():
    videos = Video.query.all()
    result = []
    for v in videos:
        result.append({
            "id": v.id,
            "camera_id": v.camera_id,
            "start_time": v.start_time.isoformat(),
            "end_time": v.end_time.isoformat(),
            "file_path": v.file_path
        })
    return jsonify(result)

# Загрузка архива
@app.route('/download', methods=['GET'])
@jwt_required()
def download_video():
    video_id = request.args.get('video_id')
    video = Video.query.get(video_id)
    if video:
        return send_file(video.file_path, as_attachment=True)
    return jsonify({"msg": "Video not found"}), 404

# Поделиться потоком
@app.route('/share-stream', methods=['POST'])
@jwt_required()
def share_stream():
    data = request.json
    stream_url = data['stream_url']
    duration = data['duration']  # в часах
    expires_at = datetime.utcnow() + timedelta(hours=duration)
    
    shared_stream = SharedStream(stream_url=stream_url, expires_at=expires_at)
    db.session.add(shared_stream)
    db.session.commit()

    share_link = url_for('access_shared_stream', stream_id=shared_stream.id, _external=True)
    return jsonify({"share_link": share_link}), 201

# Доступ к общему потоку
@app.route('/access-stream/<int:stream_id>', methods=['GET'])
def access_shared_stream(stream_id):
    shared_stream = SharedStream.query.get(stream_id)
    if shared_stream and shared_stream.expires_at > datetime.utcnow():
        return jsonify({"stream_url": shared_stream.stream_url})
    return jsonify({"msg": "Link expired or not found"}), 404
