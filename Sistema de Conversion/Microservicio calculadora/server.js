// server.js
const express = require('express');
const calcular = require('./calcular');

const app = express();
const PORT = 3000;
// Middleware para permitir CORS (solo para desarrollo, en producción configura de manera segura)
app.use((req, res, next) => {
    res.header('Access-Control-Allow-Origin', '*'); // Permitir solicitudes desde cualquier origen
    res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
    next();
});

app.use(express.json());

app.post('/calcular', (req, res) => {
    const { num1, operator, num2 } = req.body;

    if (!num1 || !operator || !num2) {
        return res.status(400).json({ error: 'Parámetros inválidos' });
    }

    const result = calcular(parseFloat(num1), operator, parseFloat(num2));
    res.json({ resultado: result });
});

app.listen(PORT, () => {
    console.log(`Servidor escuchando en el puerto ${PORT}`);
});
