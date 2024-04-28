import random

# Function to roll the dice
def roll_dice():
    return random.randint(1, 6)

# Main function to play the game
def play_ludo():
    player_total = 0
    computer_total = 0
    while True:
        input("Press Enter to roll the dice...")
        player_roll = roll_dice()
        print(f"Player rolled: {player_roll}")
        player_total += player_roll
        
        input("Press Enter for computer's turn...")
        computer_roll = roll_dice()
        print(f"Computer rolled: {computer_roll}")
        computer_total += computer_roll
        
        print(f"Player total: {player_total}")
        print(f"Computer total: {computer_total}")
        
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            break

# Main function
def main():
    print("Welcome to Ludo Dice Game :)")
    play_ludo()

# Run the main function
if __name__ == "__main__":
    main()
