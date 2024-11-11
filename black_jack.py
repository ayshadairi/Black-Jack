import random
import sys
from db import read_file


def bet_amount(money):
    while True:
        try:
            while True:
                bet = float(input("Bet amount: "))
                if bet < 5:
                    print("The minimum bet can't be smaller than 5. Please try again.")
                elif bet > 1000:
                    print("The maximum bet can't be greater than 1,000. please try again")
                elif bet > money:
                    print(f"You connot bet more than the money you have({money:.2f}). Please try again.")
                else:
                    return bet
        except ValueError:
            print("Invalid number. Please try again.")


def calculate_points(hand):
    total_points = 0
    aces = 0

    for card in hand:
        rank = card.split(' ')[0]
        if rank in ["Jack", 'Queen', 'King']:
            total_points += 10
        elif rank == "Ace":
            aces +=1
            total_points += 11
        else:
            total_points += int(rank)

    while total_points > 21 and aces > 0:
        total_points -=10
        aces -= 1
        
    return total_points



def dealer_cards(deck):
    dealer_hand = []
    card1 = random.choice(deck)
    deck.remove(card1)
    card1 = f'{card1[0]} of {card1[1]}'
    dealer_hand.append(card1)
    card2 = random.choice(deck)
    deck.remove(card2)
    card2 = f'{card2[0]} of {card2[1]}'
    dealer_hand.append(card2)

    print(f"DEALER'S SHOW CARD:\n{card1}")


    dealer_points = calculate_points(dealer_hand)

    while dealer_points < 17:
        card = random.choice(deck)
        deck.remove(card)
        card = f'{card[0]} of {card[1]}'
        dealer_hand.append(card)

        dealer_points = calculate_points(dealer_hand) 

    return dealer_hand, dealer_points

def your_cards(deck, dealer_hand, dealer_points):
    user_hand = []
    print("YOUR CARDS:")
    for _ in range(2):
        card = random.choice(deck)
        deck.remove(card)
        card = f'{card[0]} of {card[1]}'
        print(card)
        user_hand.append(card)
    user_points = calculate_points(user_hand)
    if any("Ace" in card for card in user_hand) and user_points <= 21:
        choice = input("You got an Ace! Would you like to count it as 1 or 11? ")
        if choice == "11" and user_points + 10 <= 21:
            user_points +=10
    
    
    while True:
            if user_points > 21:
                print("Bust! You went over 21.")
            print()
            choice = input("Hit or stand? (hit/Stand): ").lower()
            print()
            if choice == 'hit':
                card = random.choice(deck)
                deck.remove(card)
                card = f'{card[0]} of {card[1]}'
                user_hand.append(card)
                user_points = calculate_points(user_hand)
                print("YOUR CARDS:")
                for card in user_hand:
                    print(card)
            elif choice == 'stand':
                print("DEALER'S CARDS:")
                for card in dealer_hand:
                    print(card)
                print()
                print(f"YOUR POINTS: {user_points}")
                print(f"DEALER'S POINTS: {dealer_points}")
                break
            else:
                print("Invalid choice. Please choose again.")



    return user_hand, user_points

def determine_winner(user_points, dealer_points, money, bet):
    if user_points > 21:
        print("Sorry. You lose.")
        money = update_money(money, bet, "lose")
    elif dealer_points > 21:
        print("Congradulations! You win.")
        money = update_money(money, bet, "win")
    elif user_points > dealer_points:
        print("Congradulations! You win.")
        money = update_money(money, bet, "win")
    elif user_points < dealer_points:
        print("Sorry. You lose.")
        money = update_money(money, bet, "lose")
    else:
        print("It's a tie!")
    return money


def main():

    suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Jack', 'Queen', 'King', 'Ace']

    deck = [[rank, suit] for rank in ranks for suit in suits]
    random.shuffle(deck)
    

    
    print("BLACKJACK!")
    print("Blackjack payout is 3:2")
    print()
    while True:
        money = read_file()
        bet = bet_amount(money)
        print()
        dealer_hand, dealer_points = dealer_cards(deck)
        print()
        user_hand, user_points = your_cards(deck, dealer_hand, dealer_points)
        print()
        money = determine_winner(user_points, dealer_points, money, bet)
        print()
        again = input("Play again? (y/n): ").lower()
        print()
        if again != 'y':
            break
    print("Come back soon!")
    print("Bye!")
    
    


if __name__=="__main__":
    main()
