const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.get('/', (req, res) => {
  res.send('Bot is Running - Made by Emon Boss');
});

app.listen(PORT, () => {
  console.log('Bot Started on port ' + PORT);
});
