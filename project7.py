# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 7

def main():
    name1 = input("What's your name? ")
    print("Hello", name1, "!", "Welcome to Choose Your Own Adventure!")
    start = input("\nType start when you are ready to start playing: ")
    if (start.upper() != "START" and start.upper() != "QUIT"):
        while (start.upper() != "START" and start.upper() != "QUIT"):
            start = input("Type start to start or quit to leave: ")
            if (start.upper() == "START" or start.upper() == "QUIT"):
                break
    if (start.upper() == "START"):
        adv()
    if (start.upper() == "QUIT"):
        exit()

def adv():

    #first step 
    print("\nYou are walking in the woods and you see a crossroad.")
    a = input("Do you go left (A) or right (B)? ")
    if (a.upper() != "A" and a.upper() != "B"): #if user didn't type the right thing
        while (a.upper() != "A" and a.upper() != "B"):
            a = input("Please type A or B: ")
            if (a.upper() == "A" or a.upper() == "B"):
                break

    #option 1 for 1st 
    if (a.upper() == "A"):

        #second step
        print("\nYou turn left and see a house.")
        b = input("Do you knock (A) or break in (B)? ")
        if (b.upper() != "A" and b.upper() != "B"): #if user didn't type the right thing
            while (b.upper() != "A" and b.upper() != "B"):
                b = input("Please type A or B: ")
                if (b.upper() == "A" or b.upper() == "B"):
                    break

        #option 1 for 2nd 
        if (b.upper() == "A"):

            #third step
            print("\nYou knock but no one answers so you turn to leave when you hear a crash.")
            c = input("Do you investigate (A) or leave (B)? ")
            if (c.upper() != "A" and c.upper() != "B"): #if user didn't type the right thing
                while (c.upper() != "A" and c.upper() != "B"):
                    c = input("Please type A or B: ")
                    if (c.upper() == "A" or c.upper() == "B"):
                        break

            #option 1 for 3rd
            if (c.upper() == "A"):
                print("\nYou investigate. The crash was caused by rabid racoon that attacked you. You died.") #END1
                die()

            #option 2 for 2nd
            if (c.upper() == "B"):

                #fourth step
                print("\nYou start to leave when you hear footsteps. You feel like someone is watching you.")
                d = input("Do you go run (A) or call out (B)?")
                if (d.upper() != "A" and d.upper() != "B"): #if user didn't type the right thing
                    while (d.upper() != "A" and d.upper() != "B"):
                        d = input("Please type A or B: ")
                        if (d.upper() == "A" or d.upper() == "B"):
                            break

                #option 1 for 4th
                if (d.upper() == "A"):

                    #fifth step
                    print("\nYou start running and you hear footsteps following you.")
                    e = input("Do you hide (A) or keep running (B)")
                    if (e.upper() != "A" and e.upper() != "B"): #if user didn't type the right thing
                        while (e.upper() != "A" and e.upper() != "B"):
                            e = input("Please type A or B: ")
                            if (e.upper() == "A" or e.upper() == "B"):
                                break

                    #option 1 for 5th
                    if (e.upper() == "A"):
                        print("\nYou find a hiding spot. You wait there until you are sure the person following you is gone. You go home") #END2
                        win()

                    #option 2 for 5th
                    if (e.upper() == "B"):
                        print("\nYou keep running. You can't run fast enough. The person catches you and turns out he is the town serial killer. You die") #END3
                        die()

                #option 2 for 4th
                if (d.upper() == "B"):
                    print("\nYou call out and you see a someone walk towards it. It turns out it is your friend playing a prank on you.") #END4
                    win()

            
        #option 2 for 2nd 
        if (b.upper() == "B"):

            #third step
            print("\nYou break in by climbing in through the window. The house is very dark and you can't find any lights so you turn on the flashlight from your phone. You see one staircase going up and one going down.")
            f = input("Do you go up (A) or go down (B)? ")
            if (f.upper() != "A" and f.upper() != "B"): #if user didn't type the right thing
                while (f.upper() != "A" and f.upper() != "B"):
                    f = input("Please type A or B: ")
                    if (f.upper() == "A" or f.upper() == "B"):
                        break

            #option 1 for 3rd
            if (f.upper() == "A"):
                print("\nYou go up stairs and the lights start flickering on and off. You can't see very well. You find a room and when you walk in, you slip and fall out a window.") #END5
                die()

            #option 2 for 2nd
            if (f.upper() == "B"):

                #fourth step
                print("\nYou go downstairs to the basement when you hear a scream.")
                g = input("Do you keep looking around the basement (A) or leave the house (B)?")
                if (g.upper() != "A" and g.upper() != "B"): #if user didn't type the right thing
                    while (g.upper() != "A" and g.upper() != "B"):
                        g = input("Please type A or B: ")
                        if (g.upper() == "A" or g.upper() == "B"):
                            break

                #option 1 for 4th
                if (g.upper() == "A"):
                    print("\nYou keep looking around when you hear a door slam. Someone comes down the stairs. It's the town serial killer. You die.") #END6
                    die()

                #option 2 for 4th
                if (g.upper() == "B"):
                    print("\nYou quickly leave the house and go home.") #END7
                    win()



    #option 2 for 1st 
    if (a.upper() == "B"):

        #second step
        print("\nYou turn right and see a hotel.")
        h = input("Do you go on the top floor (A) or bottom floor (B)? ")
        if (h.upper() != "A" and h.upper() != "B"): #if user didn't type the right thing
            while (h.upper() != "A" and h.upper() != "B"):
                h = input("Please type A or B: ")
                if (h.upper() == "A" or h.upper() == "B"):
                    break

        #option 1 for 2nd 
        if (h.upper() == "A"):

            #third step
            print("\nUou go to the top floor and find a room. You sleep in the bed and get a good night's rest. The next morning when you wake up you hear a scream!")
            i = input("Do you investigate the noise (A) or do you stay in bed? (B)? ")
            if (i.upper() != "A" and i.upper() != "B"): #if user didn't type the right thing
                    while (i.upper() != "A" and i.upper() != "B"):
                        i = input("Please type A or B: ")
                        if (i.upper() == "A" or i.upper() == "B"):
                            break

            #option 1 for 3rd
            if (i.upper() == "A"):

                #fourth step
                print("\nYou investigate and find the person who made thee noise and they tell you the hotel is haunted by a ghost.")
                j = input("Do you try to catch the ghost (A) or go home (B)? ")
                if (j.upper() != "A" and j.upper() != "B"): #if user didn't type the right thing
                    while (j.upper() != "A" and j.upper() != "B"):
                        j = input("Please type A or B: ")
                        if (j.upper() == "A" or j.upper() == "B"):
                            break

                #option 1 for 4th
                if (j.upper() == "A"):
                    print("\nYou try to catch the ghost but  realize that you don't know how to catch a ghost so you call the ghostbusters. They get rid of the ghost and you go home.")  #END8
                    win()

                #option 3 for 4th
                if (j.upper() == "B"):
                    print("\nYou want to go home. You try to leave but the door does not open. The ghost trapped you. You never find a way out of the hotel.") #END9
                    die()

            #option 2 for 3rd
            if (i.upper() == "B"):
                print("\nYou go stay in bed and go back to sleep. When you wake up, you get ready to leave, but all the doors all locked. You can't find a way out of your room. You are trapped there forever.") #END10
                die()

        #option 2 for 2nd 
        if (h.upper() == "B"):
            print("You decide to go to the bottom floor. You go into the elevator, but the elevator breaks down. The elevator cable snaps and you fall to your death")
            die()


#if you die
def die():
    print("Oh No! You died!")
    dead = str(input("\nDo you want to try again? "))
    if (dead.upper() != "YES" and dead.upper() != "NO"):
        while (dead.upper() != "YES" and dead.upper() != "NO"):
            dead = str(input("Please type yes or no: "))
            if (dead.upper() == "YES" or dead.upper() == "NO"):
                break
    if (dead.upper() == "YES"):
        print("\n")
        adv()
    if (dead.upper() == "NO"):
        exit()

def win():
    print("Congrats! You made it through the game alive!")
    win = str(input("\nDo you want to play again? "))
    if (win.upper() != "YES" and win.upper() != "NO"):
        while (win.upper() != "YES" and win.upper() != "NO"):
            win = str(input("Please type yes or no: "))
            if (win.upper() == "YES" or win.upper() == "NO"):
                break
    if (win.upper() == "YES"):
        print("\n")
        adv()
    if (win.upper() == "NO"):
        exit()

if (__name__=="__main__"):
    main()
