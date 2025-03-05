import logo from './image.png';
import './App.css';
import React, { useState, useEffect } from 'react';

function App() {
  const [isVisible, setIsVisible] = useState(false);
  // usestate for setting a javascript
    // object for storing and using data

    const [name, setName] = useState('');
    const [description, setDescription] = useState('');
  
  
    
    const [data, setData] = useState({
      name1: "",
      description1: "",
      name2: "",
      description2: "",
      name3: "",
      description3: "",
    });

    

    // const [data, setData] = useState(null);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);
 
  const fetchData = async () => {
    setLoading(true);
    setError(null);
    setIsVisible(!isVisible);

    const  course = {
      name: name,
      description: description,
    }

    try {
        // Send data to the backend (POST request)
        const postResponse = await fetch('http://localhost:5000/data', {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
          },
          body: JSON.stringify(course),
        });
  
        if (!postResponse.ok) {
          throw new Error(`HTTP error! status: ${postResponse.status}`);
        }
        // const response = await fetch('http://localhost:5000/data');

        // if (!response.ok) {
        // throw new Error(`HTTP error! status: ${response.status}`);
        // }

        const json = await postResponse.json();
        // setData(json);
          setData({
            name1: json.name1,
            description1: json.description1,
            name2: json.name2,
            description2: json.description2,
            name3: json.name3,
            description3: json.description3,
          });
      
    } catch (e) {
      setError(e);
      setData(null);
    } finally {
      setLoading(false);
    }
  }
  

  return (
    <div class = "App">
      <header className='App-header'>
        <img src={logo} className="logo" alt="logo" />
      </header>

      <div className="expandable-div">
        <div>
          <label htmlFor="fname">High School Course Name:</label>
          <input type="text" id="fname" name="fname" onChange={(e) => setName(e.target.value)}/>
        </div>
        <div>
          <label htmlFor="lname">High School Course Description:</label>
          <textarea rows="5" cols="33" onChange={(e) => setDescription(e.target.value)}>
            Enter a High School Course Description
          </textarea>
        </div>
        <div>
          <button  onClick={fetchData}>Submit</button>
        </div>
      </div>
      {isVisible && 
      <div className="expandable-div">

                <h1>Most Similar College Courses</h1>
                {/* Calling a data from setdata for showing */}
                <p> 1: {data.name1}</p>
                {/* <p> 1st College Description: {data.description1}</p> */}
                <p> 2: {data.name2}</p>
                {/* <p> 2nd College Description: {data.description2}</p> */}
                <p> 3: {data.name3}</p>
                {/* <p> 3rd College Description: {data.description3}</p> */}

           
        </div>
      }
    </div>
  //   <div>
  //   <button onClick={fetchData} disabled={loading}>
  //     {loading ? 'Loading...' : 'Get Data'}
  //   </button>

  //   {error && <p>Error: {error.message}</p>}
  //   {data && (
  //     <pre>{JSON.stringify(data, null, 2)}</pre>
  //   )}
  // </div>
  );
}

export default App;
