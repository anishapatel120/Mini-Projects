import random

# Define a function to get the player's choice
def get_player_choice():
    while True:
        print("\n1. Rock")
        print("2. Paper")
        print("3. Scissors")
        choice = input("Enter your choice (1/2/3): ")
        if choice in ['1', '2', '3']:
            return int(choice)
        else:
            print("Invalid choice. Please try again.")

# Define a function to get the computer's choice
def get_computer_choice():
    return random.randint(1, 3)

# Define a function to determine the winner
def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return "It's a tie!"
    elif (player_choice == 1 and computer_choice == 3) or \
         (player_choice == 2 and computer_choice == 1) or \
         (player_choice == 3 and computer_choice == 2):
        return "You win!"
    else:
        return "Computer wins!"

# Define the main function to run the rock-paper-scissors game
def main():
    print("Welcome to Rock-Paper-Scissors Game!")
    while True:
        player_choice = get_player_choice()
        computer_choice = get_computer_choice()
        print(f"\nYour choice: {player_choice}")
        print(f"Computer's choice: {computer_choice}")
        result = determine_winner(player_choice, computer_choice)
        print(result)
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thank you for playing!")
            break

# Run the main function when the script is executed
if __name__ == "__main__":
    main()
