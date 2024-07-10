import './App.css';
import NavbarComp from "./components/Navbar"
import MainCard from './components/MainCard'
import OutputCard from './components/OutputCard'
import Hero from "./components/Hero"
import React, {useState} from 'react'; 

function App() {
  const [output, setOutput] = useState(null); 

  const handleOutputChange = (newOutput) => { 
    setOutput(newOutput)
  }
  return (
    <div className="App">
      <NavbarComp />
      <Hero />
      <div className="app-content">
        <div className="card-components" id="target-section">
          <MainCard onOutputChange={handleOutputChange}/>
        </div>
        <div className='output'>
            <OutputCard output={output}/>
        </div>
      </div>
    </div>
  );
}

export default App;
