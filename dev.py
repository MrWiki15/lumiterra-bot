from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time
import os
import signal

class ChangeHandler(FileSystemEventHandler):
    def __init__(self, command):
        self.command = command
        
        self.process = None
        self.last_modified = time.time()

    def on_any_event(self, event):
        current_time = time.time()
        if current_time - self.last_modified > 3:  # Espera 3 segundos para evitar ejecuciones múltiples
            self.restart_process()
            self.last_modified = current_time

    def restart_process(self):
        if self.process:
            print("Stopping the current process...")
            self.process.terminate()  # Terminar el proceso en Windows
            self.process.wait()  # Esperar a que termine
            print("Process stopped.")

        print(f'Running command: {self.command}')
        self.process = subprocess.Popen(self.command, shell=True)  # Iniciar el proceso en Windows

if __name__ == "__main__":
    path = "../lumiterra-bot"  # Directorio a monitorear
    command = "python bot.py"  # El comando para ejecutar tu bot

    event_handler = ChangeHandler(command)
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
