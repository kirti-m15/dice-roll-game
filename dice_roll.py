import random

def roll_dice():
    return random.randint(1,6)

def play_game():
    print("\n----DICE ROLL----")

    player1= roll_dice()
    player2= roll_dice()

    print("Player 1 rolled: ",player1)
    print("Player 2 rolled: ",player2)

    if player1 > player2:
        print("Player 1 wins! \n")
    elif player2 > player1:
        print("Player 2 wins! \n")
    else:
        print("It's a draw! \n")

def menu():
    while True:
        print("1. Play game")
        print("2. Exit \n")


        try:
            choice= int(input("enter your choice: "))
        except ValueError:
            print("INVALID INPUT! Enter a number: ")
            continue

        if choice ==1:
            play_game()
        elif choice==2:
            print("THANKS FOR PLAYING! ")
            break
        else:
            print("INVALID CHOICE! Try again.")
            
menu()