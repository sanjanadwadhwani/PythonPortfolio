def main():
    operation = input("Do you want to add, subtract, divide, or multiply? ")

    if operation.lower() == "add":
        num1 = int(input("First number: "))
        print("+")
        num2 = int(input("Second number: "))
        print("=", num1 + num2)

    if operation.lower() == "subtract":
        num1 = int(input("First number: "))
        print("-")
        num2 = int(input("Second number: "))
        print("=", num1 - num2)

    if operation.lower() == "divide":
        num1 = int(input("First number: "))
        print("/")
        num2 = int(input("Second number: "))
        print("=", num1 / num2)

    if operation.lower() == "multiply":
        num1 = int(input("First number: "))
        print("*")
        num2 = int(input("Second number: "))
        print("=", num1 * num2)


def restart():
    start = input("Would you like to do another calculation? ")


    
if (__name__=="__main__"):
    main()
