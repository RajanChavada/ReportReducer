import React, {useState, useRef} from 'react'
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faPlus } from '@fortawesome/free-solid-svg-icons';
import "./css/main.css"
import axios from 'axios'; 


export default function MainCard() {

  const [file, setFile] = useState(); 

  const inputFile = useRef(null); 

  const handleFileSubmit = () => { 
    console.log("File submitted"); 
    inputFile.current.click(); // does nothing now
  }

  function handleChange(e) {
    setFile(e.target.files[0]); 
  }

  // handle submit axios
  function handleSubmit(e) { 
    e.preventDefault(); 
    if (!file) {
      console.error('No file selected');
      return;
    }
  
    const url = 'http://127.0.0.1:5000/uploadFile';
    const formData = new FormData(); 
    formData.append('file', file); 
    formData.append('fileName', file.name); 
    const config = { 
      headers: { 
        'content-type': 'multipart/form-data',
      },
    }; 
  
    axios.post(url, formData, config)
      .then((response) => {
        console.log(response.data); 
      })
      .catch((error) => {
        console.error('Error uploading file:', error);
      });
  }
  

  return (
    <div>
      <h1>Report Reducer</h1>

      <div className="document-adder" onClick={handleFileSubmit}>
        <input 
        type='file' 
        id='file' 
        ref={inputFile} 
        style={{display: 'none'}} 
        onChange={handleChange}
        />
       <button type='submit' onClick={handleSubmit}><FontAwesomeIcon icon={faPlus} /></button>

      </div>
      

    </div>
  )
}
