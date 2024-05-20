import './App.css';
import NavbarComp from "./components/Navbar"
import MainCard from './components/MainCard'
import OutputCard from './components/OutputCard'
import Hero from "./components/Hero"

function App() {
  return (
    <div className="App">
      <NavbarComp />
      <Hero />
      <div className="app-content">
        <div className="card-components" id="target-section">
          <MainCard />
        </div>
        <div className='output'>
            <OutputCard />
        </div>
      </div>
    </div>
  );
}

export default App;
