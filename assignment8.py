# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 8

def main():
    print("Welcome to Mad Libs!")
    game = input("Choose a Mad Libs story: Vacation (A), Math Rules (B), Afraid of the Dark (C)? ")

    #if user didn't input the right thing
    if (game.upper() != "A" and game.upper() != "VACATION" and game.upper() != "B" and game.upper() != "MATH RULES" and game.upper() != "AFRAID OF THE DARK" and game.upper() != "C"):
        while (game.upper() != "A" and game.upper() != "VACATION" and game.upper() != "B" and game.upper() != "MATH RULES"):
            game = input("Please type A or B: ")
            if (game.upper() == "A" or game.upper() == "VACATION" or game.upper() == "B" or game.upper() == "MATH RULES"):
                break

    #if vacation is chosen
    if (game.upper() == "A" or game.upper() == "VACATION"):
        game1()

    #if math rules is chosen
    if (game.upper() == "B" or game.upper() == "MATH RULES"):
        game2()

    #if afraid of the dark is chosen
    if (game.upper() == "C" or gampe.upper() == "AFRAID OF THE DARK"):
        game3()

    

#vacation game
def game1():

    #title
    print("\nVacation\n")

    #inputs for blanks
    adj1 = input("Adjective? ")
    adj2 = input("Adjective? ")
    noun1 = input("Noun? ")
    noun2 = input("Noun? ")
    plnoun1 = input("Plural Noun? ")
    game = input("Name of a Game? ")
    plnoun2 = input("Plural Noun? ")
    ingv1 = input("Verb ending in ing? ")
    ingv2 = input("Verb ending in ing? ")
    plnoun3 = input("Plural Noun? ")
    ingv3 = input("Verb ending in ing? ")
    noun3 = input("Noun? ")
    plant = input("Name of a plant? ")
    body = input("Body Part? ")
    place = input("Place? ")
    ingverb4 = input("Verb ending in ing? ")
    adj3 = input("Adjective? ")
    num1 = input("Number? ")
    plnoun4 = input("Plural Noun? ")

    #story
    print("\nA vacation is when you take a trip to some", adj1, "place with your", adj2, "family.")
    print("Usually, you go to some place that is near a/an", noun1, "or up on a/an", noun2, ".")
    print("A good vacation place is one where you can ride", plnoun1, "or play", game, "or go hunting for", plnoun2, ".")
    print("I like to spend my time", ingv1, "or", ingv2, ".")
    print("When parents go on a vacation, they spend their time eating three", plnoun3, "a day, and fathers play golf, and mothers sit around", ingv3, ".")
    print("Last summer, my little brother fell in a/an", noun3, "and got poison", plant, "all over his", body, ".")
    print("My family is going to go to (the)", place, ", and I will practice", ingverb4, ".")
    print("Parents need vacations more than kids because parents are always very", adj3, "and because they have to work", num1, "hours every day all year making enough", plnoun4, "to pay for vacation.")

    end()


#math game
def game2():

    #title
    print("\nMath Rules\n")

    #inputs for blanks
    noun1 = input("Noun? ")
    noun2 = input("Noun? ")
    plnoun1 = input("Plural Noun? ")
    verb1 = input("Verb (Past Tense)? ")
    noun3 = input("Noun? ")
    adj1 = input("Adjective? ")
    adj2 = input("Adjective? ")
    noun4 = input("Noun? ")
    verb2 = input("Verb? ")
    noun5 = input("Noun? ")
    plnoun2 = input("Plural Noun? ")
    adj3 = input("Adjective? ")
    plnoun3 = input("Plural Noun? ")

    #story
    print("\n1. When a decimal is divided by a/an", noun1, "the number of decimal places in the", noun2, "is the same as the number of", plnoun1, "in the dividend.")
    print("2. The quotient is unchanged if a divisor and a dividend are each", verb1, "by the same", noun3, ".")
    print("3. If one", adj1, "number is divided by a whole numb.er, the quotient is a/an", adj2, ".")
    print("4. To find a ratio of one number to another, divide that number by the", noun4, ".")
    print("5. If you want", verb2, "two fractions, first reduce the denominators to the lowest common", noun5, ".")
    print("6. The perimeter of a rectangle is the sum of the lengths of its", plnoun2, ".")
    print("7. A/an", adj3, "fraction does not have its value changed if", plnoun3, "are added on its right.")

    end()



#afraid of the dark
def game3():

    #title
    print("\nAfraid of the Dark\n")

    #inputs for blanks
    plnoun1 = input("Plural Noun? ")
    ingv1 = input("Verb ending in ing? ")
    noun1 = input("Noun? ")
    noun2 = input("Noun? ")
    plnoun2 = input("Plural Noun? ")
    body1 = input("Body Part? ")
    noun3 = input("Noun? ")
    ingv2 = input("Verb ending in ing? ")
    body2 = input("Body Part (Plural)? ")
    ingv3 = input("Verb ending in ing? ")
    noun4 = input("Noun? ")
    noun5 = input("Noun? ")
    body3 = input("Body Part? ")
    adverb = input("Adverb? ")
    body4 = input("Body Part (Plural)? ")
    
    #story
    print("I was home alone and scared out of my", plnoun1, ".")
    print("I could hear the wind", ingv1, "and off in the distance a/an", noun1, "was howling")
    print("I crossed the room, locked the", noun2, "and climbed into the bed, pulling", plnoun2, "over my", body1, ".")
    print("Then it happened. I could hear a/an", noun3, ingv2, "up the stairs.")
    print("My", body2, "started to chatter and my knees began", ingv3, ".")
    print("The", noun4, "was thrust open and there was a huge", noun5, "with hair all over his", body3, ".")
    print('It was my father. "Hi, we are home," he said', adverb, '"Hope you were not afraid of staying home alone."')
    print('"No," I said, lying through my', body4, ".")

    end()
    
    
def end():
    play_again = str(input("\nDo you want to play again? "))
    if (play_again.upper() != "YES" and play_again.upper() != "NO"):
        while (play_again.upper() != "YES" and play_again.upper() != "NO"):
            play_again = str(input("Please type yes or no: "))
            if (play_again.upper() == "YES" or play_again.upper() == "NO"):
                break
    if (play_again.upper() == "YES"):
        print("\n")
        adv()
    if (play_again.upper() == "NO"):
        exit()

if (__name__=="__main__"):
    main()
