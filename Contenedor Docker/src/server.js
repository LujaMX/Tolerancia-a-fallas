const express = require('express');
const app = express ();

app.get('/', (req, res) =>{
res. send("Hola! Esta es la segunda versión de mi Docker");
});

app. listen (3000, function ( ) {
console. log ("app listening on port 3000");
});