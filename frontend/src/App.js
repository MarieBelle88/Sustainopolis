import React, { useEffect, useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    axios.get('http://localhost:5001/api/message')
        .then((response) => setMessage(response.data.message))
        .catch((error) => console.error('Error fetching message:', error));
  }, []);

  return (
      <div className="App">
        <header className="App-header">
          <h1>Sustainopolis</h1>
          <p>{message}</p>
        </header>
      </div>
  );
}

export default App;
