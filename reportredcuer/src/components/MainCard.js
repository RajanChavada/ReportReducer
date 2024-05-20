import React, { useState } from 'react';
import axios from 'axios';
import './css/main.css';


export default function MainCard() {
  const [file, setFile] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault(); // Prevent default form submission behavior

    if (!file) {
      setError('No file selected');
      return;
    }

    try {
      const formData = new FormData();
      formData.append('file', file);

      const response = await axios.post('http://127.0.0.1:5000/uploadFile', formData, {
        headers: {
          'Content-Type': 'multipart/form-data'
        }
      });

      console.log(response.data);
    } catch (error) {
      console.log(error)
      setError('Error uploading file: ' + error.message);
    }
  };

  return (
    <div >
      <div className='document-adder'>
        <h1>Report Reducer</h1>
        <hr></hr>
        <form onSubmit={handleSubmit}>
          <input 
            type="file" 
            onChange={handleFileChange} 
            style={{ 
              backgroundColor: 'white', 
              opacity: 0.5, 
              borderRadius: 100, 
              padding: 20, 
              margin: 20,
              display: 'flex',
              justifyContent: 'center',
              alignItems: 'center' }} 
          />
          {error && <div style={{ color: 'red' }}>{error}</div>}
          <button type="submit" disabled={!file}>Upload File</button>
        </form>
      </div>
      
    </div>
  );
}
