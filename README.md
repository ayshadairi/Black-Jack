# Blackjack Game

A simple text-based Blackjack game built using Python. This project simulates a basic Blackjack experience, where the player competes against a dealer with the goal of getting a hand total as close to 21 as possible, without exceeding it.

## Features

- **Betting System**: Players can place bets between $5 and $1000, and their balance is updated accordingly.
- **Card Deck Simulation**: A standard 52-card deck is used, with face cards (Jack, Queen, King) valued at 10 points and Aces valued as either 1 or 11.
- **Dealer AI**: The dealer follows a simple AI that hits until they reach at least 17 points.
- **Money Management**: Players can buy chips if their balance goes below $5. The player's balance is saved in a file (`money.txt`).
- **User Interaction**: The player can choose to hit or stand, and the game provides messages to guide the player through the process.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/blackjack-game.git
   ```
2. Ensure you have Python installed. This project was developed using Python 3.

3. To run the game, simply execute the Python script:

```bash
python blackjack_game.py
```
The game will create a money.txt file if it does not already exist, where the player's balance will be stored.

## Usage
- When you run the game, it will prompt you to place a bet. The minimum bet is $5, and the maximum bet is $1000.
- The game will deal two cards to you and the dealer. You can choose to either "hit" (get another card) or "stand" (end your turn).
- The dealer will play according to Blackjack rules (i.e., the dealer will keep drawing cards until they have at least 17 points).
- The game will determine the winner based on the points and update your balance.
- If your balance falls below $5, the game will prompt you to buy more chips.
## File Structure
- **blackjack_game.py:** The main Python script that runs the game.
- **money.txt:** A file used to store and update the player's balance.
