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

If no,then go to a doctor to check your eyes :P ,
but if you do, then this is because this image was encrypted with AES ECB. That means every pixel of the image was encrypted with the same key.

So if a pixel has the same color with another pixel, then the encrypted result will be the same.

Let's say we encrypt 'Hello' with AES ECB 128bit with the key `1234567891234567` which is 16 bytes key,

the result will be `3892EFAB6427AB1568092CD2262387D5` always.

So let's say black color pixels have value 'B', then if we encrypt it with key `1234567891234567`, then I will get `BC395B3316D18C490C4BABE2E6F81912` always and we can see that it's 32 bytes (cause every character in hex,has 2bytes).

You can check this video out to understand ECB systems better: https://www.youtube.com/watch?v=uPiqyQOMH1E

So our task is to find the line which has the same 32bit hex string more than 1 times.

So let's start making our python3 script!

Open,read and then split line by line the .txt file and add a line counter:
```
ciphertext = open("ctexts.txt")
ciphertext = ciphertext.read()
ciphertext = ciphertext.split('\n')

line = 0
```

Next make a loop that takes every line and splits it to 16 bytes (because the key he used to encrypt it is 16 bytes):
```
for current_hex in ciphertext:
  current_hex = wrap(current_hex, 32) # https://stackoverflow.com/questions/9475241/split-string-every-nth-character
```
