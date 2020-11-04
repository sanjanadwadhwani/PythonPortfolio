# Sanjana Wadhwani
# 1st Period
# Feb 18th, 2020
# Assignment 27

def main():

    #type function
    x = input("Type a number: ")
    print("Currently, the variable is a string. You can use the type function to see that")
    print("The input is", type(x))

    #type function, float function
    try:
        x = float(x)
        print("After converting the variable, it is now a", type(x))
    except ValueError:
        print("What you typed was not a number.")
        success = False
        while (not success):
            try:
                x = float(input("Please type a number: "))
                success = True
            except ValueError:
                print("Please type a number")

    #power function
    print("Your number to the power of five is", pow(x, 5))

    #min and max functions
    list1 = list(map(int, input("\nType a set of numbers: ").split())) #input for the data set
    print("The maximum of the set of numbers is", max(list1), "and the minimum of the set of numbers is", min(list1))
    
        
    
    
    

if (__name__=="__main__"):
          main()
