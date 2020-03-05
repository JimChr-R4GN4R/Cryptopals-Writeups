 The Base64-encoded content in ctexts.txt has been encrypted via AES-128 in ECB mode under the key

"YELLOW SUBMARINE".

(case-sensitive, without the quotes; exactly 16 characters; I like "YELLOW SUBMARINE" because it's exactly 16 bytes long, and now you do too).

Decrypt it. You know the key, after all.

Easiest way: use OpenSSL::Cipher and give it AES-128-ECB as the cipher. 

Do this with code.

You can obviously decrypt this using the OpenSSL command-line tool, but we're having you get ECB working in code for a reason. You'll need it a lot later on, and not just for attacking ECB.

################################################################

After some research I made a script for this challenge.

So just run the script <code>python3 script.py</code> and you will get the plaintext.
