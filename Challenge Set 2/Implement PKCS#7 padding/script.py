from Crypto.Cipher import AES
from Crypto.Util.Padding import pad # pip3 install PyCryptodome

block_size = 20

plaintext = b"YELLOW SUBMARINE" # length = 16

padded_plaintext = pad(plaintext, block_size)

print(padded_plaintext)