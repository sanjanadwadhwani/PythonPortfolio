# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 4


#introduction
def main():
    name = input("Hello! What is your name? ")
    print("Welcome", name, "to Rock, Paper, Scissors! I'm the computer.")
    print("Type rock, paper, or scissor. If you want to quit, type stop.") #instructions
    options = ("Rock", "Paper", "Scissors") #tuple for computer options
    print(options) 
    play()


#game
def play():
    options = ("Rock", "Paper", "Scissors") #tuple for computer options
    print("") #line break
    player = str(input("Rock, Paper, or Scissors? ")) #player input

    #if the user does not enter rock, paper, or scissors - to prevent errors
    if (player.upper() != "STOP" and player.upper() != "ROCK" and player.upper() != "PAPER" and player.upper() != "SCISSORS"):
        while (player.upper() != "ROCK" and player.upper() != "PAPER" and player.upper() != "SCISSORS"):
            player = str(input("Please type rock, paper, or scissors: "))
            if (player.upper() == "ROCK" or "PAPER" or "SCISSORS"):
                break

    #quit
    if (player.upper() == "STOP"):
        play_again()

    #computer's choice
    import random
    computer = random.choice(options)
    print(computer)

    #win and lose
    if (computer.upper() == player.upper()):
        print("We tied!", player, "Let's try again!")
        play()

    if (computer.upper() == "ROCK"):
        if (player.upper() == "PAPER"):
            win()
        if (player.upper() == "SCISSORS"):
            lose()

    if (computer.upper() == "PAPER"):
        if (player.upper() == "SCISSORS"):
            win()
        if (player.upper() == "ROCK"):
            lose()

    if (computer.upper() == "SCISSORS"):
        if (player.upper() == "ROCK"):
            win()
        if (player.upper() == "PAPER"):
            lose()


#to play again after a round
def play_again():
    play_again = str(input("Giving up already? "))
    if (play_again.upper() != "YES" and play_again.upper() != "NO"):
        while (play_again.upper() != "YES" and play_again.upper() != "NO"):
            play_again = str(input("Please type yes or no: "))
            if (play_again.upper() == "YES" or "NO"):
                break
    if (play_again.upper() == "YES"):
        print("What a chicken! >:P")
        exit()
    if (play_again.upper() == "NO"):
        print("") #line break
        play()


#when you lose
def lose():
    print("You Lose!")
    play()


#when you win
def win():
    print("You Win!")
    play()
    
                  
if (__name__=="__main__"):
    main()
