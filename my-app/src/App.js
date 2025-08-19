import logo from './image.png';
import './App.css';
import React from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import SimilaritySearch from "./SimilaritySearch";
import Home from "./Home";
import Student from "./studentView";
import Login from "./login";

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
          <Link to="/administrator" className="no-underline">Administrator</Link>
        </li>
      </ul>
      </div>
    </nav>


    <Routes>
      <Route path="/CollegeCourseMatcher" element={<SimilaritySearch />} />
      <Route path="/administrator" element={<Home />} />
      <Route path="/" element={<Student />} />
      <Route path="/login" element={<Login  />} />
    </Routes>
  </BrowserRouter>
    
 
  );
}

export default App;
