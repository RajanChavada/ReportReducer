import './App.css';
import NavbarComp from "./components/Navbar"
import MainCard from './components/MainCard'

function App() {
  return (
    <div className="App">
      <NavbarComp />
      <div className="app-content">
        <div className="card-components">
          <MainCard />
        </div>
      </div>
    </div>
  );
}

export default App;
