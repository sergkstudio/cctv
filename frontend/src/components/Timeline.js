import React, { useEffect, useState } from 'react';
import axios from 'axios';

function Timeline() {
  const [videos, setVideos] = useState([]);

  useEffect(() => {
    axios.get('/videos', {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` }
    }).then(response => {
      setVideos(response.data);
    });
  }, []);

  const downloadVideo = (id) => {
    axios.get(`/download?video_id=${id}`, {
      headers: { Authorization: `Bearer ${localStorage.getItem('token')}` },
      responseType: 'blob'
    }).then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', `video_${id}.mp4`);
      document.body.appendChild(link);
      link.click();
    });
  };

  return (
    <div>
      <h1>Видео архив</h1>
      <ul>
        {videos.map(video => (
          <li key={video.id}>
            Камера {video.camera_id}: {new Date(video.start_time).toLocaleString()} - {new Date(video.end_time).toLocaleString()}
            <button onClick={() => downloadVideo(video.id)}>Скачать</button>
          </li>
        ))}
      </ul>
    </div>
  );
}

export default Timeline;
