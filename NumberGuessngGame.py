import random

# Function to generate a random number
def generate_random_number():
    return random.randint(1, 100)

# Function to play the game
def play_game():
    random_number = generate_random_number()
    attempts = 0
    while True:
        guess = int(input("Guess the number (between 1 and 100): "))
        attempts += 1
        if guess < random_number:
            print("Too low. Try again.")
        elif guess > random_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number {random_number} correctly in {attempts} attempts.")
            break

# Main function
def main():
    print("Welcome to the Guess the Number game!")
    while True:
        play_game()
        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != 'yes':
            print("Thanks for playing!")
            break

# Run the main function
if __name__ == "__main__":
    main()
