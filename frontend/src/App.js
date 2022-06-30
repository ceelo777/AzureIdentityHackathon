import './App.css';
import {
  BrowserRouter as Router,
  Routes,
  Link,
  Route,  
} from "react-router-dom";
import InputPage from './InputPage/InputPage';
import InboxPage from './InboxPage/InboxPage';

function App() {
  return (
    <Router>
      <div className="body">
        <div className="nav-bar">
          <div className="nav-send-email">
            <Link to="/inputPage">Send Email</Link>
          </div>
          <div className="nav-scan-inbox">
            <Link to="/scanInbox">Scan Inbox</Link>
          </div>

          {/* A <Switch> looks through its children <Route>s and
              renders the first one that matches the current URL. */}        
        </div>
        <Routes>
            <Route path="/inputPage" element={<InputPage />} />
            <Route path="/users" element={<InboxPage />} />          
        </Routes>
      </div>
    </Router>
  );
}

export default App;