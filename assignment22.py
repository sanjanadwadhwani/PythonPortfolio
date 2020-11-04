# Sanjana Wadhwani
# 1st Period
# Feb 5th, 2020
# Assignment 22

def main():
    operation = input("Add, Subtract, Multiply, or Divide: ") #which operation to use
    x = str(operation) #makes input a string

    #addition
    if (x.upper() == 'ADD'):
        print("")
        print("Let's Add")
        
        #error throwing
        success = False
        while not success:
            try:
                num1 = float(input("First Number:"))
                success = True
            except ValueError:
                print("You need to type a number.")

                
        print("+")

        #error throwing
        success = False
        while not success:
            try:
                num2 = float(input("Second Number:"))
                success = True
            except ValueError:
                print("You need to type a number.")

        sum1 = add(num1, num2)
        print(num1, "+", num2, "=", sum1) #full equation
        print("") #line break
        restart()

    #subtraction
    if (x.upper() == 'SUBTRACT'):
        print("")
        print("Let's Subtract")
        #error throwing
        success = False
        while not success:
            try:
                num1 = float(input("First Number:"))
                success = True
            except ValueError:
                print("You need to type a number. ")

                
        print("-")

        #error throwing
        success = False
        while not success:
            try:
                num2 = float(input("Second Number:"))
                success = True
            except ValueError:
                print("You need to type a number.")

        difference = subtract(num1, num2)
        print(num1, "-", num2, "=", difference) #full equation
        print("") #line break
        restart()

    #multiplication
    if (x.upper() == 'MULTIPLY'):
        print("")
        print("Let's Multiply")
        
        #error throwing
        success = False
        while not success:
            try:
                num1 = float(input("First Number:"))
                success = True
            except ValueError:
                print("You need to type a number.")

                
        print("*")

        #error throwing
        success = False
        while not success:
            try:
                num2 = float(input("Second Number:"))
                success = True
            except ValueError:
                print("You need to type a number.")
                
        product = multiply(num1, num2)
        print(num1, "*", num2, "=", product) #full equation
        print("") #line break
        restart()

    #division
    if (x.upper() == 'DIVIDE'):
        print("")
        print("Let's Divide")
        
        #error throwing
        success = False
        while not success:
            try:
                num1 = float(input("First Number:"))
                success = True
            except ValueError:
                print("You need to type a number.")

                
        print("/")

        #error throwing
        success = False
        while not success:
            try:
                num2 = float(input("Second Number:"))
                success = True
            except ValueError:
                print("You need to type a number. /n")
        
        quotient = divide(num1, num2)
        print(num1, "/", num2, "=", quotient) #full equation
        print("") #line break
        restart()
                
    #if user did not type in any of the operations correctly
    else:
        print("Please either type add, subtract, multiply, or divide")
        main()


#defining the operation functions
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y
    
def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

#when done
def restart():
    restart = str(input("Would you like to do another calculation? "))
    if (restart.upper() == "YES"):
        main()
    if (restart.upper() == "NO"):
        print("Okay, bye!")
        exit()
    if (restart.upper() != "NO" or "YES"):
        while (restart.upper() != "NO" or "YES"):
            restart = str(input("Please type yes or no. Would you like to do another calculation? "))
            if (restart.upper() == "NO" or "YES"):
                break
    

if (__name__=="__main__"):
    main()
