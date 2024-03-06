print("Welcome to the Tip Calculator")

bill = float(input("What is the total bill?\n"))

tip = int(input("What percentage would you like to tip? 10, 12 or 15?\n"))

people = int(input("among how many people are you splitting?\n"))

ans= tip / 100 *bill +bill 
ans2 = ans/people
print(f"Each person should pay {round(ans2,2)}")