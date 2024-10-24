import React, { useState, useEffect } from 'react';

function App() {
  const [message, setMessage] = useState('');

  useEffect(() => {
    const backendUrl = process.env.REACT_APP_BACKEND_URL || 'http://localhost:5000';
    fetch(`${backendUrl}/api/message`)
      .then(response => response.json())
      .then(data => setMessage(data.message))
      .catch(error => console.error('Error fetching the message:', error));
  }, []);

  return (
    <div className="App">
      <h1>{message || 'Loading...'}</h1>
    </div>
  );
}

export default App;
