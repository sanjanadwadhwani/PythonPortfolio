# Sanjana Wadhwani
# 1st Period
# Feb 19th, 2020
# Assignment 24

def main():

    #open the file
    print("This is what is currently on the file.")
    f = open("periodictable.py", "r")
    print(f.read())

    #input for next two elements
    eleven = input("\nWhat is the element with the atomic number 11? ")
    if (eleven.upper() != "SODIUM"):
        print("Sorry, that is incorrect. It is sodium!")
    else:
        print("Good job! That is correct. It is sodium!")

    twelve = input("\nWhat is the element with the atomic number 12? ")
    if (eleven.upper() != "MAGNESIUM"):
        print("Sorry, that is incorrect. It is magnesium!")
    else:
        print("Good job! That is correct. It is magnesium!")

    #add the next two elements    
    print("\nElement 11 is sodium and Element 12 is magnesium")
    f = open("periodictable.py", "a")
    f.write("11: sodium \n12: magnesium")

    #printing file again
    print("\nHere is the file after adding the next two elements")
    f = open("periodictable.py", "r")
    print(f.read())
    
    

if (__name__=="__main__"):
    main()
