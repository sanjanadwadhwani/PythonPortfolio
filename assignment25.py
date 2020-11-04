# Sanjana Wadhwani
# 1st Period
# Feb 18th, 2020
# Assignment 25

def main():
    #user inputs a number

    #num1
    success = False
    while (not success):
        try:
            num = float(input("Choose a number: "))
            success = True
        except ValueError:
            print("Please type a number")
    #num2
    success = False
    while (not success):
        try:
            num1 = float(input("Choose another number: "))
            success = True
        except ValueError:
            print("Please type a number")

    #lambda functions
    double = lambda a : a * 2
    triple = lambda a : a * 3
    half = lambda a : a/2
    x = lambda a, b : a * b
    y = lambda a, b : a / b
    z = lambda a, b : a + b
    w = lambda a, b : a - b

    #number1
    print("\nNumber 1")
    print("===============")
    print("Doubled: ", double(num))
    print("Tripled: ", triple(num))
    print("Halved: ", half(num))

    #number2
    print("\nNumber 2")
    print("===============")
    print("Doubled: ", double(num1))
    print("Tripled: ", triple(num1))
    print("Halved: ", half(num1))

    #bothnumbers
    print("\nBoth")
    print("===============")
    print("Product: ", x(num, num1))
    print("Quotient: ", y(num, num1))
    print("Sum: ", z(num, num1))
    print("Difference: ", w(num, num1))
    
    

if (__name__=="__main__"):
    main()
