from textwrap import wrap

ciphertext = open("ctexts.txt") # Here you put ciphertext's file
ciphertext = ciphertext.read()

ciphertext = ciphertext.split('\n')

line = 0

for current_hex in ciphertext:

    current_hex = wrap(current_hex, 32) # https://stackoverflow.com/questions/9475241/split-string-every-nth-character
    
    line += 1

    
    ################################################################################### https://stackoverflow.com/questions/59738905/python-count-lists-values-and-put-them-in-ordered-list-without-library
    for item in set(current_hex):                                                  ##
                                                                                   #### This loop helps us to count how many items are the same in current_hex list
        if (current_hex.count(item) > 1):                                          ##
        
            listToStr = ' '.join(map(str, current_hex)).replace(' ','') # take all parts from current_hex and merge them
            
            listToStr = listToStr.replace(item,'\033[93m'+item+'\033[0m') # change color to the item which is repeated
            
            print("Found in line",line,":",listToStr)
            print()
            print('\033[91m'+item+'\033[0m', ':', current_hex.count(item),'times has been found')
            break                                                                  ##
                                                                                   ##
    #################################################################################