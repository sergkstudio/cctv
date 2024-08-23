import React, { useState } from 'react';

function Mosaic() {
  const [selectedCameras, setSelectedCameras] = useState([]);

  const cameras = ["Камера 1", "Камера 2", "Камера 3", "Камера 4"]; // замените реальными камерами

  const handleSelectCamera = (camera) => {
    setSelectedCameras(prev => {
      if (prev.includes(camera)) {
        return prev.filter(c => c !== camera);
      } else if (prev.length < 4) {
        return [...prev, camera];
      }
      return prev;
    });
  };

  return (
    <div>
      <h1>Мозаика</h1>
      <div className="mosaic">
        {selectedCameras.map((camera, index) => (
          <div key={index} className="camera-tile">
            <h3>{camera}</h3>
            {/* Вставьте сюда <video> или поток WebRTC */}
          </div>
        ))}
      </div>
      <div className="camera-selection">
        {cameras.map((camera, index) => (
          <button key={index} onClick={() => handleSelectCamera(camera)}>
            {camera}
          </button>
        ))}
      </div>
    </div>
  );
}

export default Mosaic;
