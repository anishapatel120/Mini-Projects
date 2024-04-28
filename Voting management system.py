# Database of voters
voters = {}

# Function to register a voter
def register_voter():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in voters:
        print("Voter already registered.")
    else:
        voters[username] = password
        print("Voter registered successfully.")

# Function to authenticate a voter
def authenticate_voter():
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in voters and voters[username] == password:
        print("Login successful.")
        return True
    else:
        print("Invalid username or password.")
        return False
# Function to cast a vote
def cast_vote():
    print("List of Candidates:")
    for candidate in voters:
        print(candidate)
    
    voter_choice = input("Enter the name of the candidate you want to vote for: ")
    if voter_choice in voters:
        voters[voter_choice] += 1
        print("Your vote has been cast successfully.")
    else:
        print("Invalid candidate. Please choose from the list.")

# Main function
def main():
    while True:
        print("\nVoting Management System Menu:")
        print("1. Register Voter")
        print("2. Login")
        print("3.cast a vote")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            register_voter()
        elif choice == '2':
            authenticate_voter()
        elif choice=='3':
            cast_vote()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
