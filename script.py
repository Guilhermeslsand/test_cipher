from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import subprocess
import time


class WatchHandler(FileSystemEventHandler):
    def __init__(self, script):
        self.script = script
        self.process = None
        self.run_script()

    def run_script(self):
        if self.process:
            self.process.terminate()
        print(f"\n🔁 Executando {self.script}...\n")
        self.process = subprocess.Popen(["python3", self.script])

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"🔄 Mudança detectada em {event.src_path}")
            self.run_script()


if __name__ == "__main__":
    script = "main.py"
    event_handler = WatchHandler(script)
    observer = Observer()
    observer.schedule(event_handler, ".", recursive=True)
    observer.start()
    print("👀 Observando mudanças nos arquivos...")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
