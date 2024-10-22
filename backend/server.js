const express = require('express');
const cors = require('cors');

const app = express();
const port = 5000;

app.use(cors());

app.get('/api/data', (req, res) => {
  const messages = [
    'Hello from the backend!',
    'This is another message.',
  ];
  res.json(messages);
});

app.listen(port, () => {
  console.log(`Server listening on port ${port}`);
});
