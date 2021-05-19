#funtion for encryption,it takes the plain text string and the shift variable/number as input and returns the encrypted text
def encrypt(str, shift):

    cipher = ''
    for char in str:
        if char == ' ':                                                    #to deal with spaces 
            cipher = cipher + char
        elif char.isupper():
            cipher = cipher + chr((ord(char) + shift - 65) % 26 + 65)       #we use 65 as its ASCII for uppercase and then the rest of it is the simple formula for encryption
        else:
            cipher = cipher + chr((ord(char) + shift - 97) % 26 + 97)       #we use 97 as its ASCII for lowercase and then the rest of it is the simple encryption formula

    return cipher

#funtion for decryption,it takes the encrypted string and the shift variable/number as input and returns the decrypted text
def decrypt(str, shift):

    word = ''
    for char in str:
        if char == ' ':
            word = word + char
        elif char.isupper():
            word = word + chr((ord(char) - shift - 65) % 26 + 65)       #we use 65 as its ASCII for uppercase and then the rest of it is the simple formula for decryption
        else:
            word = word + chr((ord(char) - shift - 97) % 26 + 97)       #we use 97 as its ASCII for lowercase and then the rest of it is the simple decryption formula

    return word

#driver code to get input from the user and get output from the functions
#we use if and elif loops to give the user the choice of encrypting or decrypting the text
c = input("if you want to encrypt press e,if u want to decrypt press d ")
if c == 'e':                                                                #loop to send control to encrypt function
    text = input("enter string: ")
    s = int(input("enter shift number: "))
    print("original string: ", text)
    print("after encryption: ", encrypt(text, s))
elif c == 'd':                                                               #loop to send control to decrypt function
    text = input("enter encrypted text: ")
    s = int(input("enter shift number: "))
    print("encrypted text: ", text)
    print("after decryption: ", decrypt(text, s))
