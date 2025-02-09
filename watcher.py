#Importar librerias y funciones como watchdog,python-dotenv
import time 
import shutil 
#Manejo del sistema 
import os 
#Variables de entorno 
from dotenv import load_dotenv
#Librerias para el observador de carpetas
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
#Funcion para convertir los pdf a OCR 
from create_pdf import new_pdf
#Funcion para asignar nombre 
from anchors import anchors 

#Carga de variables del sistema
load_dotenv() 


#Clase para manejar los eventos de el sistema de lectura 
class event_manager (FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".pdf"):
            print(f"Nuevo archivo detectado: {event.src_path}")
            #Ruta del pdf para hacer OCR
            ruta = event.src_path.replace("\\", "/")

            #Funcion para crear el nuevo OCR
            new_pdf(ruta, ruta) 

            #Asignar nombre 
            ancla = anchors(ruta) 

            nombre = ancla[0] 

            os.rename(ruta, f"C:/Users/User/Documents/Python/docs_revisados/{nombre}.pdf") 

            print(f"Documento movido a C:/Users/User/Documents/Python/docs_revisados/{nombre}") 


#Funcion para el monitoreo de la carpeta 
def monitor_folder(path):
    manager = event_manager()
    watcher = Observer()
    watcher.schedule(manager, path, recursive=False)
    watcher.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        watcher.stop()
    watcher.join()

path = os.getenv("MY_PATH")

monitor_folder(path) 