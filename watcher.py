#Importar librerias y funciones como watchdog,python-dotenv
import time 
import shutil 
import os 
from dotenv import load_dotenv
from watchdog.observers import Observer 
from watchdog.events import FileSystemEventHandler
#Funcion para leer documentos 
from pdf import pdf_reader
from create_pdf import new_pdf

#Carga de variables del sistema
load_dotenv() 


#clase para manejar los eventos de el sistema de lectura 
class event_manager (FileSystemEventHandler):
    def on_created(self, event):
        if event.src_path.endswith(".pdf"):
            print(f"Nuevo archivo detectado: {event.src_path}")
            contenido = pdf_reader(event.src_path)
            print(f"Contenido del PDF: \n{contenido}")
 
            read = os.getenv("NEW_PATH")
            new_path = os.path.join(read, os.path.basename(event.src_path))
            shutil.move(event.src_path, new_path)
            print(f"Archivo movido a {new_path}")

            #Variable de entorno para crear el nuevo pdf
            pdf = os.getenv("NEW_PDF")
            new_pdf(contenido, pdf)  

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