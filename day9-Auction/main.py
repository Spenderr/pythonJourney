import os
print("\nWelcome to secret Bid program\n\n")
bidders = True
bidlist={}
while bidders:
    name = input("What is your name:") 
    bid = int(input("What is your bid:"))
    x = input("Are there any other bidders? Type 'y' for Yes or 'n' for No:")
    bidlist[name] = bid
    if x == "n" or x == "N":
        bidders = False
    else:
        os.system('clear')
        print("Now for the next person")


maxBid = 0
for key in bidlist:
    if bidlist[key] > maxBid:
        maxBid = bidlist[key]
        ansName = key



print(f"The winner of auction is {ansName} with a bid of {maxBid}")
