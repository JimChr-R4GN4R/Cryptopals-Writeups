from Crypto.Cipher import AES
 
key = '1234567891234567'
 
cipher = AES.new(key.encode('utf8'), AES.MODE_ECB)


##########################################################
msg =cipher.encrypt('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')  ### plaintext = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
                                                         #
                                                         #
print('aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa =',msg.hex())    ### ciphertext = 19311a27364dc24db32547a989bb26d819311a27364dc24db32547a989bb26d8
##########################################################
print()
##########################################################
msg =cipher.encrypt('aaaaaaaaaaaaaaaa')                  ### plaintext = 'aaaaaaaaaaaaaaaa'
                                                         #
                                                         #
print('aaaaaaaaaaaaaaaa =',msg.hex())                    ### ciphertext = 19311a27364dc24db32547a989bb26d8
##########################################################
