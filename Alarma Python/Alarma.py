import datetime
import time
import pygame

import win32serviceutil
import win32service
import win32event

def sonar_alarma():
    pygame.mixer.init()
    # Obtener la hora actual
    hora_actual = datetime.datetime.now().time()

    # Establecer la hora a las 5:00 PM
    hora_alarma = datetime.time(17, 0, 0)  # 17 representa las 5:00 PM en formato de 24 horas

    # Calcular la cantidad de segundos hasta la alarma
    timeAlarma = datetime.datetime.combine(datetime.date.today(), hora_alarma) - datetime.datetime.combine(datetime.date.today(), hora_actual)
    secondsAlarma = timeAlarma.total_seconds()

    # Esperar hasta la hora de la alarma
    time.sleep(secondsAlarma)

    pygame.mixer.music.load('alarma.mp3')
    pygame.mixer.music.play()

    time.sleep(10)

    # Detener la reproducción de la alarma
    pygame.mixer.music.stop()

    print("¡Hora de Hacer TAREA!")

class ServicioAlarma(win32serviceutil.ServiceFramework):
    _svc_name_ = "ServicioAlarma"
    _svc_display_name_ = "Alarma Tarea"
    _svc_description_ = "Este servicio me recuerda hacer tarea a las 5 PM."

    def __init__(self, args):
        win32serviceutil.ServiceFramework.__init__(self, args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)

    def SvcDoRun(self):
        self.ReportServiceStatus(win32service.SERVICE_START_PENDING)
        self.ReportServiceStatus(win32service.SERVICE_RUNNING)
        self.main()

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)

    def main(self):
        while True:
            # Coloca aquí el código de tu servicio
            sonar_alarma()

if __name__ == '__main__':
    win32serviceutil.HandleCommandLine(ServicioAlarma)