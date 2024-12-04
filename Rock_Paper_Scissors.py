import random

def get_computer_choice():
    """Randomly selects the computer's choice."""
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)

def get_user_choice():
    """Prompts the user for their choice."""
    while True:
        choice = input("Enter your choice (rock, paper, scissors): ").lower()
        if choice in ["rock", "paper", "scissors"]:
            return choice
        else:
            print("Invalid choice. Please choose 'rock', 'paper', or 'scissors'.")

def determine_winner(user_choice, computer_choice):
    """Determines the winner of the game."""
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    """Main game loop."""
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"\nYou choose: {user_choice}")
        print(f"Computer choose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(f"Result: {result}\n")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye.")
            break

# Run the game
if __name__ == "__main__":
    play_game()
