import random

def users_card():
    return random.randrange(0, 13)

def dealers_card():
    return random.randrange(1, 12)

def multiplier():
    return random.uniform(1.1, 1.5)

def new_line():
    print("\n")

def rules():
    print("Rules:")
    print("1. You will be shown the dealer's number. Guess if your number will be higher or lower.")
    print("2. If you win, you earn a multiplier on your bet. If you lose, the bet is lost.")
    print("3. Initial money is 500. Minimum bet is 10.")
    print("4. Bonus rounds (every 5th round): Multiplier is 2, and dealer's number is 7.")
    print("5. Type 'yes' or 'no' to make choices.")
    print("6. Press Enter without typing to exit.\n")

def get_amount(INITIAL_MONEY,MIN_BET):

    try:
        boot = float(input("Enter your bet amount : "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return None

    if boot <= 0:
        print("Bet must be greater than 0.")
        return None

    elif boot > INITIAL_MONEY:
        print(f"money insufficient {boot-INITIAL_MONEY} more needed")
        return None
    
    elif boot < MIN_BET:
        print (f"bet amount must be greater than {MIN_BET}")
        return None
    else:
        return boot


INITIAL_MONEY = 500.0
MIN_BET = 10.0

money = INITIAL_MONEY
round_number = 1
playing = True

print(rules())

new_line()
new_line()

while True:

    print("."*40)

    if round_number%5==0:

        print("\tBONUS ROUND ",round_number)
        first_multiplier = 2
        first_card = 7
    
    else:
        print("\t\tROUND ",round_number)
        first_multiplier = multiplier()
        first_card = dealers_card()

    new_line()

    print(f"Current Money :{money:.2f}")

    new_line()

    boot = get_amount(money,MIN_BET)

    while boot is None:
        new_line()
        boot = get_amount(INITIAL_MONEY,MIN_BET)
        continue

    new_line()

    print(f"Dealer's Card is : {first_card}")
    print(f"Multiplier : {first_multiplier:.2f}")

    global choice

    while True:
        
        choice = input("Will the next card be higher? (yes/no)\n==>")
        if choice.strip().lower() in ['yes', 'y']:
            choice = True
            break
        elif choice.strip().lower() in ['no', 'n']:
            choice = False
            break
        else:
            print("Invalid choice. Please type 'yes' or 'no'.")
            continue

    new_line()

    player_card = users_card()
    print(f"your card is : {player_card}")

    new_line()

    if choice == True:
        
        if (player_card>first_card):
            
            money1 = (boot*first_multiplier)-boot
            
            print(f"you won : {money1:.2f}")
        
        else:

            money1 = -boot
            print(f"you lost : {money1:.2f}")

    elif choice == False:
        
        if (player_card<first_card):
            
            money1 = (boot*first_multiplier)-boot
            
            print(f"you won : {money1:.2f}")
            
        else:
            money1 = -boot
            print(f"you lost : {money1:.2f}")

    money+=money1

    if money <= 0:
        print("Game Over! You've lost all your money :(")
        break
    
    new_line()

    continue_playing = input("Do you want to play another round? : ").strip().lower()
    if continue_playing != "yes":
        print("Thank you for playing!")
        print("."*40)
        break

    round_number += 1

print("."*40)
new_line()
print(f"Final balance: {money:.2f}")
print(f"Profit/Loss: {money - INITIAL_MONEY:.2f}")
new_line()
print("."*40)





