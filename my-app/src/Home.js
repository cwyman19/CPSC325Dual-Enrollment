import logo from './image.png';
import './Home.css';
import React, { useState, useEffect } from 'react';
import { BrowserRouter, Routes, Route, Link } from 'react-router-dom';
import SimilaritySearch from "./SimilaritySearch";
import DataTable from "./new";

function Home() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [selectedDescription, setSelectedDescription] = useState(null); // State to store selected description
  
  
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('http://localhost:5000/table');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const json = await response.json();
        setData(json);
        setLoading(false);
      } catch (e) {
        setError(e);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <p>Loading...</p>;
  }

  if (!data || data.length === 0) {
    return <p>No data to display.</p>;
  }

  const headers = Object.keys(data[0]);

  const handleDescriptionClick = (description) => {
    setSelectedDescription(description); // Store the clicked description in state
  };

  const closeDescription = () => { 
    setSelectedDescription(false);
  }

  return (
    <div className="table-div" >
      <table>
        <thead>
          <tr>
            {headers.map((header) => (
              <th key={header}>
                {header === "College Course Description" || header === "HS Course Description" ? (
                  <span className="course-description-header">{header}</span>
                ) : (
                  header
                )}
              </th>
            ))}
          </tr>
        </thead>
        <tbody>
          {data.map((row, index) => (
            <tr key={index}>
              {headers.map((header) => (
                <td key={header}>
                  {header === "College Course Description" || header === "HS Course Description" ? (
                    <a 
                      href="#!" 
                      className="description-link"
                      onClick={() => handleDescriptionClick(row[header])}  // Set the clicked description
                    >
                      View Description
                    </a>
                  ) : (
                    row[header]
                  )}
                </td>
              ))}
            </tr>
          ))}
        </tbody>
      </table>

      
      {selectedDescription && (
        <div className="description-modal">
          <div className="modal-content">
            <span 
              className="close" 
              onClick={() => setSelectedDescription(null)}  
            >
              &times;
            </span>
            <h3>Course Description</h3>
            <p>{selectedDescription}</p>
            <button onClick={closeDescription}> Exit </button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Home;


