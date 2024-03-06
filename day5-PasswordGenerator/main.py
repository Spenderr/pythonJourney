import random


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to password generator")

let_no = int(input("how many letters would you like?:"))
sym_no = int(input("how many symbols would you like?:"))
num_no = int(input("How many numbers do you want?:"))

lets =0
syms = 0
nums = 0

password = ""
loop = let_no+sym_no+num_no
x= 0
while x < loop:

    y = random.randint(1,3)

    if y == 1 and lets != let_no:
        password += letters[random.randint(0,len(letters)-1)]
        lets+=1
    elif y == 1 and lets == let_no:
        x-=1
    
    if y == 2 and syms != sym_no:
        password += symbols[random.randint(0,len(symbols)-1)]
        syms+=1 
    elif y == 2 and syms == sym_no:
        x-=1

    if y == 3 and nums != num_no:
        password += numbers[random.randint(0,len(numbers)-1)]
        nums+=1
    elif y == 3 and nums == num_no:
        x-=1

    x+=1


print("\n\nYour password:",password)
