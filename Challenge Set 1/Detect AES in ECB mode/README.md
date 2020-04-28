`ctexts.txt` In this file are a bunch of hex-encoded ciphertexts.

One of them has been encrypted with ECB.

Detect it.

Remember that the problem with ECB is that it is stateless and deterministic; the same 16 byte plaintext block will always produce the same 16 byte ciphertext. 

######################################################################

So let's begin!

First of all we have to understand what ECB actually is...

![image1](https://raw.githubusercontent.com/pakesson/diy-ecb-penguin/master/Tux_ecb.png)

Do you see this image?

Can you recognize what it shows?

If no,then go to doctor to check you eyes :P ,
but if you do, then this is because this image was encrypted with AES ECB. That means every pixel of the image was encrypted with the same key.

So if a pixel has the same color with another pixel, then the encrypted result will be the same.

Let's say we encrypt 'Hello' with AES ECB 128bit with the key `1234567891234567` which is 16bit key.

The result will be `3892EFAB6427AB1568092CD2262387D5` always.

So let's say black color pixels have value 'B', then if we encrypt it with key `1234567891234567`, then I will get `BC395B3316D18C490C4BABE2E6F81912` always.

You can check this video out to understand ECB systems better: https://www.youtube.com/watch?v=uPiqyQOMH1E
