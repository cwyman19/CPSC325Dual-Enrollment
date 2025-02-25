import logo from './image.png';
import './App.css';
import React, { useState } from 'react';


function App() {
  const [isExpanded, setIsExpanded] = useState(false);

  
   // Function to toggle the expansion state
   const toggleExpansion = () => {
    setIsExpanded(!isExpanded);
  };
  
  return (
    <div className="App">
    <header className="App-header">
      <img src={logo} className="logo" alt="logo" />
      {/* className="App-logo" */}
      {/* <p>
        Edit <code>src/App.js</code> and save to reload.
      </p> */}
       <a
          className="App-link"
          // href="https://reactjs.org"
          // target="_blank"
          // rel="noopener noreferrer"
        >
        
        </a>
     
    </header>
    <div
        className={`expandable-div ${isExpanded ? 'expanded' : ''}`}
      >
    <form id="courseForm">
        <label for="fname">High School Course Name:</label><br></br>
        <input type="text" id="fname" name="fname"></input><br></br>
        <label for="lname">High School Course Description:</label><br></br>
        <textarea rows="5" cols="33">
              Enter a High School Course Description
        </textarea><br></br>
        <button onClick={toggleExpansion}>  Submit </button> 
    </form>
    </div>
  </div>
  );
  
  
  
}


export default App;
