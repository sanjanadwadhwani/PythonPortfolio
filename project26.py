# Sanjana Wadhwani
# 1st Period
# Feb 18th, 2020
# Assignment 26

def main():

    #error-throwing and get the number from input
    success = False
    while (not success):
        try:
            num = int(input("Type an integer smaller than -20: "))

            #make sure number is smaller
            if (num > -20):
                while (num > -20):
                    num = int(input("Type an integer smaller than -20: "))
                    if (num < -20):
                        break
            success = True
            
        except ValueError:
            print("Please type a number")

    #absvalue
    print("\nThe absolute value of your number is", abs(num))

    #make a bit
    print("\nThe abs value of your number as a binary number is", bin(abs(num)))

    #split input
    list1 = list(map(int, input("\nType a set of numbers: ").split())) #input for the data set

    #sum of input
    print("The sum of your data set is", sum(list1))
    
    
    

if (__name__=="__main__"):
          main()
