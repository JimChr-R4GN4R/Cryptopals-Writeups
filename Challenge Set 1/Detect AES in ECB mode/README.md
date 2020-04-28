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

You can check this video out to understand ECB systems better: https://www.youtube.com/watch?v=uPiqyQOMH1E

By having the above in your mind, let's take this example:

we have our `plaintext1 = 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'` (which is 'a' 32 times to be multiple of 16) because `block size = 16`.

And we have `plaintext2 = 'aaaaaaaaaaaaaaaa'` (which is 'a' 16 times).


If we encrypt them with `key = '1234567891234567'`, then we will take these: 

```
ciphertext1 = 19311a27364dc24db32547a989bb26d819311a27364dc24db32547a989bb26d8
ciphertext2 = 19311a27364dc24db32547a989bb26d8
```

hmmm... Do you see something...?

No? Let's split them by 32.

```
ciphertext1 = 19311A27364DC24DB32547A989BB26D8 19311A27364DC24DB32547A989BB26D8
ciphertext2 = 19311A27364DC24DB32547A989BB26D8
```
This is a sign of AES ECB encryption!

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
  
  line += 1 # line = line + 1
```

Next we want to compare all the parts of `current_hex` and count the same parts and if a part is appeared more than one times,then print the current_hex with the number of the line you found it:
```
for current_hex in ciphertext:
  current_hex = wrap(current_hex, 32) # https://stackoverflow.com/questions/9475241/split-string-every-nth-character
  
  line += 1 # line = line + 1
  

  for item in set(current_hex):
    
        if (current_hex.count(item) > 1):
        
            listToStr = ' '.join(map(str, current_hex)).replace(' ','') 
            
            listToStr = listToStr.replace(item,'\033[93m'+item+'\033[0m')
            
            print("Found in line",line,":",listToStr)
            print()
            print('\033[91m'+item+'\033[0m', ':', current_hex.count(item),'times has been found')
            break
```

Done!

Now if you are new with AES ECB, then you may have a question...
If I have a plaintext which is smaller or generally not multiple by key's length, then what happens?
The answer is `Padding`!

Check this video out : https://www.youtube.com/watch?v=R3NosHMSi0o and your question will be answerd from 2:45 ,
and check this out after the video: http://hextodecimal.com/index.php?hex=0B , it may help ;)
