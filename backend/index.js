const express = require('express');
const app = express();
const port = 5000;

app.use(express.json());

app.get('/api/data', (req, res) => {
  res.json({ message: 'Hello from backend!' });
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
