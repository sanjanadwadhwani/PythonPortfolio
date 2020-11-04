# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 2


def main():
    #strings
    name = input("What is your name? ")
    print("Hello,", name)

    #lists
    list1 = [3, 4, 6, 7]
    print("This is a list: ", list1)
    num1 = int(input("Type a number to add to the list: "))
    list1.append(num1)
    print(list1)

    #tuples
    tup1 = (1, 4, "hello", 5)
    print("This is a tuple: ", tup1)
    
    #multiply function
    z = int(input("What number do you want to multiply by 50? "))
    answer = multiply (z, 50)
    print(z, "* 50 = ", answer)
    
def multiply(x, y):
    return x * y

if (__name__=="__main__"):
    main()
