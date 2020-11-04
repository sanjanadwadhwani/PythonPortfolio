# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 12

#introduction
def main():
    print("Welcome to Hangman! You can choose how many lives you want. It \nwill show you how many lives you have, what you have guessed, \nwhat letters you have guessed in the word, and the number of \nletters in the word. Then, type the letter you want to guess \nIt will tell you if you are wrong or right.")
    begin = input("\nType start to begin: ")
    if (begin.upper() != "START"):
        while (begin.upper() != "START"):
            begin = input("Type start to begin: ")
            if (begin.upper == "START"):
                break
    if (begin.upper() == "START"):
        hangman()

#game
def hangman():
    pwords = ["today", "octopus", "password", "tomato", "airplane", "science"] #word options
    import random
    word = random.choice(pwords)

    #beginning values
    global lives
    guesses = []
    numfails = 0
    numoflives()
    if (lives > 20):
        while (int(lives) > 20):
            lives = input("Too high of a number. Please choose a number less than 20: ")
            if (int(lives) < 20):
                break
    wordtoguess = []
    rightguesses = []
    for letter in word:
        wordtoguess.append("_")

    #loop for game
    done = False
    while not done:
        livesleft = lives-numfails
        if (livesleft == (0)):
            print("You are out of lives. You lost")
            print("The word was", word)
            done = True #done because lost
            break
        print("")
        print("Lives Left: ", livesleft)
        print("Your Guesses: ", guesses)
        print("Current Word: ", ''.join(wordtoguess))
        print("Number of Letters in Word: ", len(word))
        print("")
        guess = str(input("Guess a Letter: "))
        if (guess.upper() == "WORD"):
            while (guess.upper() == "WORD"):
                word_guess = str(input("What do you think the word is?"))
                if (word_guess == word):
                    guess = word
                    print("You won! The word was", word)
                    done = True #done because win
                if (word_guess != word):
                    print("You are wrong.")
                    numfails +=1
                    print("")
                    print("Lives Left: ", livesleft)
                    print("Your Guesses: ", guesses)
                    print("Current Word: ", ''.join(wordtoguess))
                    print("Number of Letters in Word: ", len(word))
                    print("")
                    guess = str(input("Guess a Letter: "))

        #if letter has already been guesses
        for i in range(0, len(guesses)):   
            if (guesses[i] == guess):
                while (guesses[i] == guess):
                    guess = input("You already guessed this letter. Choose another one: ")
                    if (guesses[i] != guess):
                        break

        #if not a letter
        if not (guess.isalpha()):
            while not guess.isalpha():
                guess = input("\nNot a letter. Try again: ")
                if (guess.isalpha()):
                    break

        guesses.append(guess)

        #tracking letters
        if (guess in word):
            print("\nCorrect")
        if (guess not in word):
            print("\nWrong")
            numfails += 1
        for i in range(0, len(word)):   
            if (word[i] == guess):
                wordtoguess[i] = guess
                rightguesses.append(wordtoguess[i])
        if (''.join(wordtoguess) == word):
            print("You won! The word was", word)
            done = True #done because you won

    playagain()

def numoflives():
    global lives
    try:
        lives = input("How many lives do you want? ")
        int(lives)
    except ValueError:
        print("That is not a valid integer.")
        numoflives()
    lives = int(lives)


#play again after you are done
def playagain():
    x = input("Would you like to try again? ")
    if (x.upper() != "YES" and x != "NO"):
        while (x.upper() != "YES" and x.upper() != "NO"):
            x = input("Invalid answer. Type yes or no.")
            if (x == "YES" or x == "NO"):
                break
    if (x.upper() == "YES"):
        main()
    if (x.upper() == "NO"):
        print("Thanks for playing")
        exit()

if (__name__ == "__main__"):
    main()
            


