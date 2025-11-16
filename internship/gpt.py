import random

def guessing_game():
    print("Welcome to the Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    secret_number = random.randint(1, 100)
    attempts = 0
    
    while True:
        guess = int(input("Enter your guess: "))
        attempts += 1
        
        if guess < secret_number:
            print("Too low. Try again.")
        elif guess > secret_number:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts!")
            break

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']
    wins = 0
    for _ in range(5):
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()
        computer_choice = random.choice(choices)
        
        if user_choice not in choices:
            print("Invalid choice. Try again.")
            continue
        
        print(f"You chose {user_choice}. Computer chose {computer_choice}.")
        
        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == 'rock' and computer_choice == 'scissors') or \
             (user_choice == 'paper' and computer_choice == 'rock') or \
             (user_choice == 'scissors' and computer_choice == 'paper'):
            print("You win!")
            wins += 1
        else:
            print("Computer wins!")
    
    print(f"You won {wins} out of 5 rounds.")

def main():
    print("Choose a game:")
    print("1. Guessing Game")
    print("2. Rock, Paper, Scissors")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        guessing_game()
    elif choice == '2':
        rock_paper_scissors()
    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
