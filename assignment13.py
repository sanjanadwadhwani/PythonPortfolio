# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 13

def main():

    #INDEFINITE ITERATION
    #checks to make sure input is a number
    success = False 
    while not success:
        try:
            x = input("Type a number: ")
            float(x)
            success = True
        except ValueError:
            print("You did not type a number.\n")
    print("You typed a number! Thank you!")
    x = float(x)
    n1 = x

    success = False 
    while not success:
        try:
            y = input("\nHow many times do you want to multiply that number by 2? ")
            int(y)
            success = True
        except ValueError:
            print("You did not type a integer.\n")
    y = int(y)
    

    #DEFINITE ITERATION
    for i in range(y):
        x = x * 2
    print("") #line break
    print(n1, "multiplied by two", y, "times is equal to", x)
        

if (__name__=="__main__"):
    main()
