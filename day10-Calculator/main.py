
#add 
def add(n1,n2):
    return n1+n2

#subtract
def subtract(n1,n2):
    return n1-n2

def multiply(n1,n2):
    return n1*n2

def divide(n1,n2):
    return n1/n2

operations = {
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}



print("Welcome")

num1 = int(input("What is the first Number:"))
num2 = int(input("What is the second Number:"))
calculate = True

for x in operations:
    print(x)

operation = input("Select an operation:")
calculation = operations[operation]
print(f"{num1} {operation} {num2} = {calculation(num1,num2)}")
num2 = calculation(num1,num2)

while calculate:
    
    ans = input("Do you want to continue calculating (y or n):")
    if ans == 'y':
        continue
    elif ans == 'n':
        calculate = False
        break
    operation = input("Select another operation:")
    calculation = operations[operation]
    num3 = int(input("Enter another number:"))
    print(f"{num2} {operation} {num3} = {calculation(num2,num3)}")
    num2 = calculation(num2,num3)

print("goodbye")