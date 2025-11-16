import random
def rockpapersiccors():
    print("***ROCK PAPER SCISSORS***")
    options=['ROCK','PAPER','SCISSORS']
    M= random.choice(options)
    c=input("Enter your choise :").upper()
    if (c=="ROCK"and M=="PAPER") or (c=="PAPER" and M=="SCISSORS") or (c=="SCISSORS"  and M=="ROCK"):
        print("you lost...the game")
        print(f"computer choise={M}")
    elif c==M:
        print("tie break...")
        print(f"computer choise={M}")
    else:
        print("you wonnn....")
        print(f"computer choise={M}")

def guessnumber():
    machine=random.randint(1,10)
    guess=int(input('enter your choice'))
    while machine!=guess:
        if guess<machine:
            print("think big")
            guess=int(input('enter your choice'))
        elif guess>machine:
            print("think small")
            guess=int(input('enter your choice'))
        else:
            break
        print("eyyyyyyyuuuuuuu")

def main():
    print("Choose a game:")
    print("1. Guessing Game")
    print("2. Rock, Paper, Scissors")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        rockpapersiccors()     
    elif choice == '2':
        guessnumber()
    else:
        print("Invalid choice. Please enter 1 or 2.")
        if __name__ == "__main__":
            main()
        
