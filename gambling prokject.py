import random
slot1 = random.randint(1,10)
slot2 = random.randint(1,10)
slot3 = random.randint(1,10)
wallet = 1000
wallet = int(wallet)
moneymaker = input("do you want to spin?\n")
moneymaker = "y"
while "y" in moneymaker:
    slot1 = random.randint(1,10)
    slot2 = random.randint(1,10)
    slot3 = random.randint(1,10)
    print(slot1, slot2, slot3)
    if slot1 == slot2 == slot3:
        print("BIG WIN SUPER JACKPOT YESSSSSSSSSSSSSSSSSSSSSSSSSSSSSSS!!!!")
        moneymaker = input("do you want to spin?\n")
        moneymaker = "y"
        wallet += 2000
    elif slot1 == slot2:
        print("JACKPOT!!")
        wallet += 20
        print("you have",wallet,"left KEEP SPINNING")
        moneymaker = input("do you want to spin?\n")
        moneymaker = "y"
    elif slot1 == slot3:
        print("mini JACKPOT!!")
        wallet += 5
        print("you have",wallet,"left KEEP SPINNING")
        moneymaker = input("do you want to spin?\n")
        moneymaker = "y"
    elif slot2 == slot3:
        print("JACKPOT!!")
        wallet += 20
        print("you have",wallet,"left KEEP SPINNING")
        moneymaker = input("do you want to spin?\n")
        moneymaker = "y"
    elif slot1 != slot2 != slot3:
        print("you lose KEEP GOING!!")
        wallet -= 5
        print("you have",wallet,"left KEEP SPINNING")
        moneymaker = input("do you want to spin?\n")
        moneymaker = "y"
if wallet <= 0:
    print("you have lost alot of money...\n")
    loan = input("do you want to take out a loan? ")
    if loan == "yes":
        moneymaker = input("do you want to spin?\n")
        
        
    