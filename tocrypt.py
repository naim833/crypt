import cryptography
from cryptography.fernet import Fernet

key=b''

input_file ='test.txt'
output_file ='test.txt.encrypted'
with open(input_file, "rb") as file:
     data=file.read    

fernet = Fernet(key)
encrypted = fernet.encrypt(data)
with open(filename, "wb") as file:
     file.write(encrypted)
