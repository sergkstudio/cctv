import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import Timeline from './components/Timeline';
import Mosaic from './components/Mosaic';
import Login from './components/Login';

function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/timeline" element={<Timeline />} />
        <Route path="/mosaic" element={<Mosaic />} />
      </Routes>
    </Router>
  );
}

export default App;
