# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
from art import logo

print(logo)
cont = True
dict = {}
while cont:
    name = input("Enter your name: ")
    bit = int(input("Enter your Bit $"))
    dict[name]= bit
    next_bit = input("Are there any other bidders? Type 'yes or 'no'.").lower()
    print("\n" * 20)
    if next_bit == "no":
        cont = False

highest_bit = 0
winner = ""
for i in dict:
    bitting_amount = dict[i]
    if bitting_amount > highest_bit:
        highest_bit = bitting_amount
        winner = i

print(f"The winner is {winner} with a bid of {highest_bit}")
    