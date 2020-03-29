import base64
from Crypto.Cipher import AES



ciphertext = open("text.txt") # Here you put ciphertext's file
ciphertext = ciphertext.read()

ciphertext = base64.b64decode(ciphertext)

key = 'YELLOW SUBMARINE' # here you put the key /// 16, 24 or 32 bytes long for AES-128, AES-192 or AES-256 

decipher = AES.new(key, AES.MODE_ECB)

decrypted_text = decipher.decrypt(ciphertext)

print(decrypted_text.decode())



#print(ciphertext)
