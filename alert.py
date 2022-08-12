import psutil # task manager
import time # intervalos de tiempo
from datetime import datetime
from os import path # rutas relativas
from notifypy import Notify # notificaciones
import sys # manda parametros

def shoot_noti():
    print("Se cerró la aplicacion => ", datetime.now().strftime("%H:%M:%S"))
    noti.send()

def check_software():
    return sys.argv[1] not in (p.name() for p in psutil.process_iter())

direccion_abs = path.abspath(path.dirname(__file__))

audio = "Mario-Muerte.wav"

noti = Notify(
    default_notification_title="HEEEEEY!",
    default_notification_message="Se cerró " + sys.argv[1] + ", Levántalo!!",
    default_notification_audio=path.join(direccion_abs,audio)
    )

while(True):
    if check_software():
        shoot_noti()
        time.sleep(20) # Espera 20 segundos"
    time.sleep(8) 
