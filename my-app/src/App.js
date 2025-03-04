import logo from './image.png';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [isExpanded, setIsExpanded] = useState(false);
  // usestate for setting a javascript
    // object for storing and using data

    const [data, setdata] = useState({
      name1: " Computer Application Essentials INFO 101",
      description1: "",
      name2: "",
      description2: "",
      name3: "",
      description3: "",
  });

  const toggleExpand = () => {
    setIsExpanded(!isExpanded);
  };

  

  useEffect(() => {
    fetch("http://localhost:5000/data")
      .then((res) => {
        if (!res.ok) {
          throw new Error("Network response was not ok");
        }
        return res.json();
      })
      .then((data) => {
        console.log("Fetched data:", data);  // Ensure data is fetched correctly
  
        // Try a simple alert just with the name to verify
        setTimeout(() => {
          alert("Data fetched: " + data.Name);  // Just showing the Name as a basic test
        }, 0);
  
        // Setting the fetched data to the state
        setdata({
          name: data.Name,
          age: data.Age,
          date: data.Date,
          programming: data.programming,
        });
      })
      .catch((error) => {
        console.error("Error fetching data:", error);
      });
  }, []);
  
  

  return (
    <div class = "App">
      <header className='App-header'>
        <img src={logo} className="logo" alt="logo" />
      </header>

      <div className="expandable-div">
        <div>
          <label htmlFor="fname">High School Course Name:</label>
          <input type="text" id="fname" name="fname" />
        </div>
        <div>
          <label htmlFor="lname">High School Course Description:</label>
          <textarea rows="5" cols="33">
            Enter a High School Course Description
          </textarea>
        </div>
        <div>
          <button onClick={toggleExpand}>Submit</button>
        </div>
      </div>
      <div className="App">

                <h1>React and flask</h1>
                {/* Calling a data from setdata for showing */}
                <p>{data.name}</p>
                <p>{data.age}</p>
                <p>{data.date}</p>
                <p>{data.programming}</p>

           
        </div>
    </div>
  );
}

export default App;
