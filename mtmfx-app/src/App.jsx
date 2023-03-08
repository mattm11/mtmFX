import NavigationBar from "./components/NavigationBar";
import { BrowserRouter, Route, Routes } from 'react-router-dom'
import Home from "./pages/Home";
import Dashboard from "./pages/Dashboard";
import Footer from "./components/Footer";

function App() {

  return (
    <>
      <BrowserRouter>
        <div id="app-holder">
          <NavigationBar />
          <div className="container">
            <Routes>
              <Route exact path="/" element={<Home />}></Route>
              <Route exact path="/dashboard" element={<Dashboard />}></Route>
            </Routes>
          </div>
          <Footer />
        </div>
      </BrowserRouter>
    </>
  );
}

export default App;
