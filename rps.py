# Exercise 8

import getpass

def game():
    print("Rock Paper Scissors")
    p1 = input("Enter first player name: ")
    p2 = input("Enter second player name: ")
    
    m1 = getpass.getpass("Player 1's move: ")
    m2 = getpass.getpass("Player 2's move: ")

    if m1.lower() == "scissors":
        if m2.lower() == "scissors":
            return "P1: Scissors\nP2: Scissors\nDraw"
        elif m2.lower() == "rock":
            return "P1: Scissors\nP2: Rock\n" + p2 + " wins!"
        elif m2.lower() == "paper":
            return "P1: Scissors\nP2: Paper\n" + p1 + " wins!"
        else:
            return "Wrong input"
        
    elif m1.lower() == "paper":
        if m2.lower() == "paper":
            return "P1: Paper\nP2: Paper\nDraw"
        elif m2.lower() == "scissors":
            return "P1: Paper\nP2: Scissors\n" + p2 + " wins!"
        elif m2.lower() == "rock":
            return "P1: Paper\nP2: Rock\n" + p1 + " wins!"
        else:
            return "Wrong input"
        
    elif m1.lower() == "rock":
        if m2.lower() == "rock":
            return "P1: Rock\nP2: Rock\nDraw"
        elif m2.lower() == "scissors":
            return "P1: Rock\nP2: Scissors\n" + p1 + " wins!"
        elif m2.lower() == "paper":
            return "P1: Rock\nP2: Paper\n" + p2 + " wins!"
        else:
            return "Wrong input"
        
print(game())