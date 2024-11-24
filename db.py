import sys

# this function is for reading the file that contains the money
def read_file():
    try:
        with open("money.txt", 'r') as file:
            line = file.readline().strip()
            money = float(line)
            print("Money:", money)
            return money
    except FileNotFoundError:
        print("Could not find the file named money.txt. Exiting the program")
        sys.exit()
    except Exception as e:
        print(type(e),e)
        print("Closing program")
        sys.exit()

# this will calculate the money if the user wins/loses and write the changes to the file
def update_money(money, bet, result):
    if result == "win":
        money += bet * 1.5
        money = round(money,2)
    elif result == "lose":
        money -= bet
    with open("money.txt", 'w') as file:
        file.write(f"{money:.2f}")

    print(f"Money: {money:.2f}")
    return money

# this function is for saving any changes to the file
def save_money(money):
    with open("money.txt", "w") as file:
        file.write(f"{money:.2f}")
