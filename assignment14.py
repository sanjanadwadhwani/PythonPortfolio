# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 14


#introduction
def main():
    name = input("Hello! What is your name? ")
    print("\nWelcome", name, "to Guess the Number.")
    print("I will choose a integer between 1 and 100. You guess a integer and I will tell you if it is higher or lower than that number.") #instructions
    play()

def play():
    global x
    import random
    x = random.randint(1, 101)
    guesses()

def guesses():

    #input is number
    success = False 
    while not success:
        try:
            guess = input("\nWhat is your guess? ")
            int(guess)
            success = True
        except (ValueError):
            print("You did not type an integer.\n")
    guess = int(guess)

    if (guess == x): #you winn
        win()
    else:
        if (guess > x): #number is too big
            print("Your number is too big")
            guesses()
        else:
            if (guess < x): #number is too small
                print("Your number is too small")
                guesses()


#when you win
def win():
    print("\nYou got it!")
    done = str(input("\nDo you want to play again? "))
    if (done.upper() != "YES" and done.upper() != "NO"):
        while (done.upper() != "YES" and done.upper() != "NO"):
            done = str(input("Please type yes or no: "))
            if (done.upper() == "YES" or done.upper() == "NO"):
                break
    if (done.upper() == "YES"):
        print("A new number has been selected")
        play()
    if (done.upper() == "NO"):
        exit()

               
if (__name__=="__main__"):
    main()
