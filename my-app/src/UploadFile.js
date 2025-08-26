import React, { useState } from "react";

function UploadFile() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);
  const [visible, setVisible] = useState(false);
  const [printJson, setJson] = useState(false);
  const handleFileChange = (e) => {
    const selectedFile = e.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
    }
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    if (!file) {
      alert("Please select a file first!");
      return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
      const response = await fetch("https://cpscdualenrollmentbackend.onrender.com/upload", {
        method: "POST",
        body: formData,
      });

      if (!response.ok) {
        throw new Error(`HTTP error! status: ${response.status}`);
      }
      const json = await response.json();
      setJson(json)
      setVisible(true);
    } catch (err) {
      setError(err.message);
    }
  };

  return (
    <div>
      <form onSubmit={handleSubmit}>
        <input type="file" onChange={handleFileChange} />
        <button type="submit">Upload</button>
      </form>
      {visible && <p>Successfully Uploaded File</p>}
      {error && <p>Error: {error} {printJson}</p>}
    </div>
  );
}

export default UploadFile;

