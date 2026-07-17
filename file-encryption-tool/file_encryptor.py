from cryptography.fernet import Fernet

# Generate a key
key = Fernet.generate_key()

# Save the key
with open("secret.key", "wb") as key_file:
    key_file.write(key)

cipher = Fernet(key)

# Read original file
with open("secret.txt", "rb") as file:
    original_data = file.read()

# Encrypt data
encrypted_data = cipher.encrypt(original_data)

# Save encrypted file
with open("secret.txt.enc", "wb") as encrypted_file:
    encrypted_file.write(encrypted_data)

print("File encrypted successfully!")

# Decrypt data
decrypted_data = cipher.decrypt(encrypted_data)

# Save decrypted file
with open("secret_decrypted.txt", "wb") as decrypted_file:
    decrypted_file.write(decrypted_data)

print("File decrypted successfully!")