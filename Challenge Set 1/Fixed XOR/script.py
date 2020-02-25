a = '1c0111001f010100061a024b53535009181c'
b = '686974207468652062756c6c277320657965'


def XOR(a_hex,b_hex):
  a_binary = bin(int(a_hex, 16))[2:] # convert from hex to binary
  b_binary = bin(int(b_hex, 16))[2:] # convert from hex to binary
  a_binary_XOR_b_binary = int(a_binary,2) ^ int(b_binary,2) # a_binaryXOR_b_binary is in decimal format
  a_binary_XOR_b_binary = hex(a_binary_XOR_b_binary).split('x')[-1] # convert from decimal to hex
  print(a_binary_XOR_b_binary)


XOR(a,b)

# https://stackoverflow.com/questions/1425493/convert-hex-to-binary
# https://stackoverflow.com/questions/3283984/decode-hex-string-in-python-3
# https://stackoverflow.com/questions/11119632/bitwise-xor-of-hex-numbers-in-python
# https://stackoverflow.com/questions/19414093/how-to-xor-binary-with-python
# https://stackoverflow.com/questions/5796238/python-convert-decimal-to-hex
