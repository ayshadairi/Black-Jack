import sys

def read_file():
    try:
        with open("money.txt", 'r') as file:
            line = file.readline().strip()
            money = float(line)
            print("Money:", money)
            return money
    except FileNotFoundError:
        print("Could not find the file named money.txt")
        exit_program()
        
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
