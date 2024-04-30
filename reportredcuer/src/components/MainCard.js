import React, { useState } from 'react';
import axios from 'axios';
import './css/main.css'

export default function MainCard() {
  const [file, setFile] = useState(null);

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async () => {
    if (!file) {
      console.error('No file selected');
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
      console.error('Error uploading file:', error);
    }
  };

  return (
    <div className='document-adder'>
      <h1>Report Reducer</h1>
      <hr></hr>
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
      <button onClick={handleSubmit}>Upload File</button>
    </div>
  );
}
