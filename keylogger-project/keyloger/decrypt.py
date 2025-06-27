from cryptography.fernet import Fernet

# Load key
with open('key.key', 'rb') as f:
    key = f.read()

fernet = Fernet(key)

# Read encrypted logs
with open('log.txt', 'rb') as f:
    lines = f.readlines()

# Decrypt and print
for line in lines:
    try:
        print(fernet.decrypt(line.strip()).decode())
    except:
        print("❌ Could not decrypt a line")
