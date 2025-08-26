import './Home.css';
import React, { useState, useEffect } from 'react';
import { useNavigate } from 'react-router-dom';
import { BrowserRouter as Router, Route, Link, Routes } from 'react-router-dom';

function Home() {
  const [data, setData] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedDescription, setSelectedDescription] = useState(null); // State to store selected description
  const [searchInput, setSelectedInput] = useState(""); 
  const [error, setError] = useState(null);
  const [filter1, setFilter1] = useState("");
  const [filter2, setFilter2] = useState("");
  const [filter3, setFilter3] = useState("");
  const [filter4, setFilter4] = useState("");
  const [filter5, setFilter5] = useState("");
  const [filter6, setFilter6] = useState("");
  const [filter7, setFilter7] = useState("");
  const navigate = useNavigate();
  const [filters, setFilters] = useState({ name: '', category: '' });
  const [hasResults, setHasResults] = useState(true);
  const [highschoolInput, setHighschoolInput] = useState([]);
  const [collegeInput, setCollegeInput] = useState([]);
  const [schoolDistrict, setSchoolDistrictInput] = useState([]);
  const [careerCluster, setCareerClusterInput] = useState([]);
  const [status, setStatusInput] = useState([]);
  const [academicYear, setAcademicYearInput] = useState([]);
  const [alphabetical, setAlphabeticalInput] = useState([]);
  useEffect(() => {
    const fetchData = async () => {
      try {
        const response = await fetch('https://cpscdualenrollmentbackend.onrender.com/table');
        const highSchoolResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/highschoolFilter');
        const collegeResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/collegeFilter');
        const schoolDistrictResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/schooldistrictFilter');
        const careerClusterResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/careerclusterFilter');
        const academicYearResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/academicyearFilter');
        const statusResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/statusFilter');
        const alphabeticalResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/adminalphabeticalFilter');
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const json = await response.json();
        const highSchooljson = await highSchoolResponse.json();
        const collegejson = await collegeResponse.json();
        const schoolDistrictjson = await schoolDistrictResponse.json();
        const careerClusterjson = await careerClusterResponse.json();
        const academicYearjson = await academicYearResponse.json();
        const statusjson = await statusResponse.json();
        const alphabeticaljson = await alphabeticalResponse.json();
        setData(json);
        setHighschoolInput(highSchooljson);
        setCollegeInput(collegejson);
        setSchoolDistrictInput(schoolDistrictjson);
        setCareerClusterInput(careerClusterjson);
        setAcademicYearInput(academicYearjson);
        setStatusInput(statusjson);
        setAlphabeticalInput(alphabeticaljson);
        setLoading(false);
      } catch (e) {
        setError(e);
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  
  
  const headers = (Array.isArray(data) && data.length > 0)
  ? Object.keys(data[0])
  : [];

  const handleDescriptionClick = (description) => {
    setSelectedDescription(description); // Store the clicked description in state
  };

  const closeDescription = () => { 
    setSelectedDescription(false);
  }
  const search = async (event) => {
    if (event.keyCode === 13) {
        const obj = {filters, searchInput};
        setLoading(true);
        try {
            // Send data to the backend (POST request)
            const postResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/search', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(obj),
        });
  

        if (!postResponse.ok) {
            throw new Error(`HTTP error! status: ${postResponse.status}`);
        }
      

        const json = await postResponse.json();
        setData(json);
        setLoading(false);
        setHasResults(json.length > 0);
        } catch (e) {
            setError(e);
            setData(null);
        } finally {
            setLoading(false);
        }
    }
  }


  const handleFilterChange = async (e) => {
    const { name, value } = e.target;
  
    // Update filters object
    const updatedFilters = { ...filters, [name]: value };
    setFilters(updatedFilters);
    
    // Also update individual filter state
    if (name === "highschool") setFilter1(value);
    if (name === "college") setFilter2(value);
    if (name === "schooldistrict") setFilter3(value);
    if (name === "careercluster") setFilter4(value);
    if (name === "academicyear") setFilter5(value);
    if (name === "status") setFilter6(value);
    if (name === "alphabetical") setFilter7(value);
    setLoading(true);
    try {
      const postResponse = await fetch('https://cpscdualenrollmentbackend.onrender.com/filter', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(updatedFilters),
      });
  
      if (!postResponse.ok) {
        throw new Error(`HTTP error! status: ${postResponse.status}`);
      }
  
      const json = await postResponse.json();
      setData(json);
      setHasResults(json.length > 0); 
    } catch (e) {
      setError(e);
      setData(null);
    } finally {
      setLoading(false);
    }
  };
   
  

  return (
    <div className="table-div" >
  <div className="search-container">
    <div className="spacer" /> 
    <div className="button-container"> 
    <Link to="/CollegeCourseMatcher">
      <button> College Course Matcher </button> 
    </Link>
    </div>
    <div className="filter-wrapper">
    
    <div>
    <select 
      className="filter" 
      name="highschool" 
      value={filter1} 
      onChange={handleFilterChange}
    >
      <option value="">Choose a High School</option>
      {highschoolInput.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
      
    </select>

    
    <select 
      className="filter" 
      name="college"
      value={filter2} 
      onChange={handleFilterChange}
    >
      <option value="">Choose a College</option>
      {collegeInput.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
    </select>
    <select 
      className="filter" 
      name="schooldistrict"
      value={filter3} 
      onChange={handleFilterChange}
    >
      <option value="">Choose a School District</option>
      {schoolDistrict.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
    </select>
    <select 
      className="filter" 
      name="careercluster"
      value={filter4} 
      onChange={handleFilterChange}
    >
      <option value="">Choose a Career Cluster</option>
      {careerCluster.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
    </select>
    <select 
      className="filter" 
      name="academicyear"
      value={filter5} 
      onChange={handleFilterChange}
    >
      <option value="">Choose a Academic Year</option>
      {academicYear.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
    </select>
    <select 
      className="filter" 
      name="status"
      value={filter6} 
      onChange={handleFilterChange}
    >
      <option value="">Choose a Status</option>
      {status.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
    </select>
    <select 
      className="filter" 
      name="alphabetical"
      value={filter7} 
      onChange={handleFilterChange}
    >
      <option value="">Order By</option>
      {alphabetical.map((item, index) => (
        <option value={item} key={index}>{item}</option>
      ))}
    </select>
    </div>
  </div>
  
  <div className="search-box-wrapper">
    <input
      className="searchInput"
      type="text"
      placeholder="Search..."
      onChange={(e) => setSelectedInput(e.target.value)}
      onKeyDown={search}
    />
  </div>
</div>
  
{hasResults && (
  <div>
{!loading && (
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
)}
      {loading && (
        <p>Loading...</p>
      )}

      
      
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
)}
{!hasResults && (
  <p>No data to display.</p>
)}
    </div>

  );


}

export default Home;


