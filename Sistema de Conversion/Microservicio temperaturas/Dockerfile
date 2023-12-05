# Dockerfile

# Usa la imagen oficial de Node.js
FROM node:14

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos de la aplicación
COPY package*.json ./
COPY convertidorTemperaturas.js ./
COPY server.js ./

# Instala las dependencias
RUN npm install

# Expone el puerto
EXPOSE 3000

# Inicia la aplicación
CMD ["node", "server.js"]