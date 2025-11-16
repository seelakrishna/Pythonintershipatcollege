import random
choise=input("enyer your choise (A/B):").upper()
if choise=="A":
    print("***Number game***")
    machine = random.randint(1,10)
    guess= int(input("enter your choise(1-10):"))
    while machine!=guess:
        if guess < machine:
            print("oops lesser number...")
            guess=int(input("enter your choise(1-10):"))
        elif guess > machine:
            print("oops greater number...")
            guess=int(input("enter your choise(1-10):"))
        else:
            break
    print("eyyyyyuuuuuuuuuuu......... ")
elif choise=="B":
    print("***ROCK PAPER SCISSORS***")
    options=['ROCK','PAPER','SCISSORS']
    M= random.choice(options)
    c=input("Enter your choise IN ROCK PAPER SCISSORS):").upper()
    if (c=="ROCK"and M=="PAPER") or (c=="PAPER" and M=="SCISSORS") or (c=="SCISSORS"  and M=="ROCK"):
        print("you lost...the game")
        print(f"computer choise={M}")
    elif c==M:
        print("tie break...")
        print(f"computer choise={M}")
    else:
        print("you wonnn....")
        print(f"computer choise={M}")
