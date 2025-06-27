from cryptography.fernet import Fernet

key = Fernet.generate_key()

# Save key to key.key file
with open("key.key", "wb") as key_file:
    key_file.write(key)

print("✅ Key generated and saved in key.key!")
