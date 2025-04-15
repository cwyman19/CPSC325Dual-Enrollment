import logo from './image.png';
import './App.css';
import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import SimilaritySearch from "./SimilaritySearch";
import Home from "./Home";

function App() {
  return (
    <BrowserRouter>
    <nav class = "App">
      <header className='App-header'>
            <img src={logo} className="logo" alt="logo" />
      </header>
      <div className = "contents">
      <ul >
        <li>
          <Link to="/" className="no-underline">Home</Link>
        </li>
        <li>
          <Link to="/SimilaritySearch" className="no-underline">Similarity Search</Link>
        </li>
      </ul>
      </div>
    </nav>


    <Routes>
      <Route path="/SimilaritySearch" element={<SimilaritySearch />} />
      <Route path="/" element={<Home />} />
    </Routes>
  </BrowserRouter>
    
 
  );
}

export default App;
