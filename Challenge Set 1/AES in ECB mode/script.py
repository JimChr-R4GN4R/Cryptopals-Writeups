import base64
from Crypto.Cipher import AES
key = b'YELLOW SUBMARINE'

with open('ctexts.txt') as texts:
  ciphertext = base64.b64decode(texts.read())

  cipher = AES.new(key, AES.MODE_ECB)
  plaintext = cipher.decrypt(ciphertext)
  print(plaintext)
