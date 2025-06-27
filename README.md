# 🛡️ Defender Project – Encrypted Keylogger with Decryption GUI

> **Note:** This project is strictly for educational and ethical purposes only. Do not use on any system without explicit permission.

---

## 📌 Description

The **Defender Project** is a proof-of-concept keylogger built with Python that securely captures keystrokes, encrypts them using `Fernet` encryption, and stores them in a log file. A user-friendly **PyQt5 GUI** is provided to decrypt and view logs in a safe, readable format.

---

## 🎯 Features

- 🔐 Real-time keylogging using `pynput`
- 🧪 Encrypted logging with `cryptography.fernet`
- 📁 Secure log storage (`log.txt`)
- 🖥️ GUI-based decryption with PyQt5
- 📂 File selection and error handling
- 📄 Timestamped log entries Tools & Libraries

- Python 3.10+
- [pynput](https://pypi.org/project/pynput/)
- [cryptography](https://pypi.org/project/cryptography/)
- [PyQt5](https://pypi.org/project/PyQt5/)

---
 Project Structure
 keylogger-project/
├── keylogger.py # Records encrypted keystrokes
├── gui.py # GUI to decrypt/view logs
├── key.key # Encryption key file
├── log.txt # Encrypted logs
└── decrypted_log.txt # Output of decrypted logs

yaml
Copy
Edit

---

## 🚀 How to Run

### 1. Install Dependencies
```bash
pip install pynput cryptography PyQt5
2. Run the Keylogger
bash
Copy
Edit
python keylogger.py
3. Run the GUI to Decrypt Logs
bash
Copy
Edit
python gui.py
