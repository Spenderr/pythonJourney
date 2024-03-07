alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'e' to encrypt, type 'd' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(text,shift):
    newString = ""
    for x in range(0,len(text)):
        #print(ord(text[x]))
        if ord(text[x])-97-shift >= len(alphabet):
            shirtftIndex =  ord(text[x])-97-shift +26
        else:
            shirtftIndex = ord(text[x])-97-shift

        if text[x] == " ":
            newString+=" "
        else:
            newString+=alphabet[shirtftIndex]
    print("Your decrypted text:"+newString)


def encrypt(text,shift):
    newString = ""    
    for x in range(0,len(text)):
        #print(ord(text[x]))
        if ord(text[x])-97+shift >= len(alphabet):
            shirtftIndex =  ord(text[x])-97+shift -26
        else:
            shirtftIndex = ord(text[x])-97+shift

        if text[x] == " ":
            newString+=" "
        else:
            newString+=alphabet[shirtftIndex]
    print("Your encrypted text:"+newString)

if direction == "e":
    encrypt(text,shift)
elif direction == "d":
    decrypt(text,shift)   




