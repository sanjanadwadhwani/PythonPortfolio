# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 9

def main():
    #intro
    print("Inputs are always string")
    x = input("For example type a number: ")
    print("Right now x =", x)
    print("If I try to do any calculation with the input, it won't work.")
    print("X * 5 =", x*5)

    #convert to integer
    print("\nIn order to do math with it, I would convert it to an integer.")
    x = int(x)
    print("X * 5 =", x*5)

    #convert to floating number
    print("\nBut integers never have decimals.")
    z = input("Type a number with a decimal: ")
    print("Right now z =", z, "If I try to convert it to an integer, there will be an error.")
    print("Instead you can convert it to a floating point number by saying float(z) like this: z =", float(z))

    #convert integer to binary
    print("\nYou can also convert an integer to binary")
    print("To convert the x from earlier, (x =", x, "), you say bin(x)")
    print(bin(x))

    #what type
    print("\nIf you want to know the type a variable is all you have to do is type type(x)")
    print("x is", type(x))
    print("z is", type(z))
    
    

    
if (__name__=="__main__"):
    main()
