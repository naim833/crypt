from cryptography.fernet import Fernet
f = Fernet(key)
filename='test.txt.encrypted'
with open(filename, "rb") as file:

    encrypted_data = file.read()
    decrypted_data = f.decrypt(encrypted_data)
d='test.txt'
with open(d, "wb") as file:
     file.write(decrypted_data)
