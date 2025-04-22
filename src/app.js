const express = require('express');
const app = express();

app.get('/', (req,res) => {
    res.send("Welcome to my Generation-GH AWS cloud Intensive program")
})


const PORT = 3000;
const HOST = '0.0.0.0'; // Listen on all interface

app.listen(PORT, HOST, () => {
  console.log(`Server running at http://${HOST}:${PORT}/`);
});