import binascii

encoded = binascii.unhexlify('1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736')

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'] 

score_table = [8.167,1.492,2.202,4.253,12.702,2.228,2.015,6.094,6.966,0.153,1.292,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.356,2.758,0.978,2.560,0.150,1.994,0.077,8.167,1.492,2.202,4.253,12.702,2.228,2.015,6.094,6.966,0.153,1.292,4.025,2.406,6.749,7.507,1.929,0.095,5.987,6.327,9.356,2.758,0.978,2.560,0.150,1.994,0.077] # https://en.wikipedia.org/wiki/Letter_frequency

for xor_key in range(1,256):
  decoded = ''.join(chr(b ^ xor_key) for b in encoded)
  final_score = 0

  counter_for_score = 0
  for i in alphabet:
    letter_count = 0
    letter_count += decoded.count(i)
    letter_score = letter_count * score_table[counter_for_score]
    final_score += letter_score
    counter_for_score += 1
  
  if decoded.isprintable():
    if final_score > 0: # because if final_score is 0, that means all the text is unreadable too
      print(xor_key,":", decoded,":",final_score)
