`ctexts.txt` In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext. 

######################################################################

So let's begin!

First of all we have to understand what ECB actually is...

!image1(https://raw.githubusercontent.com/pakesson/diy-ecb-penguin/master/Tux_ecb.png)
