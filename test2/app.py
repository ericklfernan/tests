# app.py
import os
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#-----------------------------------------------------------------------------------
app_version = os.environ.get('APP_VERSION', 'Unknown')
environment = os.environ.get('ENVIRONMENT', 'Unknown')
print(f"Running App version {app_version} in {environment} environment.")
#-----------------------------------------------------------------------------------

#-----------------------------------------------------------------------------------
class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f"File created: {event.src_path}")

    def on_modified(self, event):
        if event.is_directory:
            return
        print(f"File modified: {event.src_path}")

#-----------------------------------------------------------------------------------

# Set the path to the folder you want to monitor
folder_path = '/app/data'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, path=folder_path, recursive=False)

#-----------------------------------------------------------------------------------
print(f"Monitoring folder: {folder_path}")
observer.start()
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    observer.stop()

observer.join()
