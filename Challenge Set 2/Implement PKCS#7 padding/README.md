Implement PKCS#7 padding

A block cipher transforms a fixed-sized block (usually 8 or 16 bytes) of plaintext into ciphertext. But we almost never want to transform a single block; we encrypt irregularly-sized messages.

One way we account for irregularly-sized messages is by padding, creating a plaintext that is an even multiple of the blocksize. The most popular padding scheme is called PKCS#7.

So: pad any block to a specific block length, by appending the number of bytes of padding to the end of the block. For instance,

`"YELLOW SUBMARINE"`

... padded to 20 bytes would be:

`"YELLOW SUBMARINE\x04\x04\x04\x04"`

###########################################################


So, if you have checked the `Detect AES in ECB mode` from `set 1`, you have a question how padding works.

There are many differrent padding methods. Here we will see PKCS#7.

So we have our `plaintext = "YELLOW SUBMARINE"`

our `plaintext` has `length = 16`. If our `block size = 20`, then we have to fill the rest 4 blocks.

So PKCS#7 methods says that the rest blocks will be filled with the hex number of the rest blocks (here the number of the rest blocks is `4`).

So the padded plaintext should be like this: b'YELLOW SUBMARINE\x04\x04\x04\x04'
