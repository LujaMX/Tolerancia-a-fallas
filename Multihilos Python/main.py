import threading
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


from pytube import YouTube
# URL del video que deseas descargar

# Función 1: Imprimir números del 1 al 5
def descargarVideo():
    url = 'https://www.youtube.com/watch?v=kinQsc6y9Kw'
    # Crear un objeto YouTube
    yt = YouTube(url)

    # Seleccionar la mejor resolución disponible
    video = yt.streams.get_highest_resolution()
    #video.download(output_path='/ruta/de/destino/')          DIRECTORIO DEFINIDO

    # Descargar el video
    video.download(filename="video.mp4")

    print("Descarga completada.")

def descargarCancion():
        url = 'https://www.youtube.com/watch?v=LOZJugltLRs'
        # Crear una instancia de la clase YouTube
        yt = YouTube(url)

        # Seleccionar la mejor resolución disponible (en este caso, el audio)
        stream = yt.streams.filter(only_audio=True).first()

        # Descargar el video
        stream.download(filename="cancion.mp3")

        # Renombra el archivo a una extensión .mp3

        print("Descarga completada")

# Función 3: Imprimir números del 6 al 10
def descargarVideo2():
    url = 'https://www.youtube.com/watch?v=4wh9dPmjAnU'
    # Crear un objeto YouTube
    yt = YouTube(url)

    # Seleccionar la mejor resolución disponible
    video = yt.streams.get_highest_resolution()
    #video.download(output_path='/ruta/de/destino/')          DIRECTORIO DEFINIDO

    # Descargar el video
    video.download(filename="video2.mp4")

    print("Descarga completada.")


# Crear hilos para cada función
hilo1 = threading.Thread(target=descargarVideo)
hilo2 = threading.Thread(target=descargarCancion)
hilo3 = threading.Thread(target=descargarVideo2)

# Iniciar los hilos
hilo1.start()
hilo2.start()
hilo3.start()

# Esperar a que todos los hilos terminen
hilo1.join()
hilo2.join()
hilo3.join()

print('Programa terminado')