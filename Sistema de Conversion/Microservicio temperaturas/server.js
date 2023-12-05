// server.js
const express = require('express');
const convertirTemperatura = require('./convertidorTemperaturas');

const app = express();
const PORT = 3000;

// Middleware para permitir CORS (solo para desarrollo, en producción configura de manera segura)
app.use((req, res, next) => {
  res.header('Access-Control-Allow-Origin', '*'); // Permitir solicitudes desde cualquier origen
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept');
  next();
});

app.use(express.json());

app.post('/convertirTemperatura', (req, res) => {
  const { temperatura, conversionType } = req.body;

  if (!temperatura || !conversionType) {
    return res.status(400).json({ error: 'Parámetros inválidos' });
  }

  const result = convertirTemperatura(parseFloat(temperatura), conversionType);
  res.json({ resultado: result });
});

app.listen(PORT, () => {
  console.log(`Servidor escuchando en el puerto ${PORT}`);
});