import random

print("Welcome to Rock, Paper, Scissors Game!")

while True:
    user_score = 0
    computer_score = 0
    rounds = 5  # number of rounds

    for i in range(rounds):
        print(f"\nRound {i+1} of {rounds}")
        user_choice = input("Enter your choice (rock/paper/scissors): ").lower()
        options = ["rock", "paper", "scissors"]
        computer_choice = random.choice(options)

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        elif user_choice not in options:
            print("Invalid input! Please choose rock, paper, or scissors.")
        else:
            print("Computer wins this round!")
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

    print("\nFinal Result")
    print(f"Your Score: {user_score}")
    print(f"Computer Score: {computer_score}")

    if user_score > computer_score:
        print("You are the overall winner!")
    elif user_score < computer_score:
        print("Computer wins the game!")
    else:
        print("It’s a tie overall!")

    # Ask to play again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("Thanks for playing!")
        break