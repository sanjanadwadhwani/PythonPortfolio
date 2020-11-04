# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 10

def main():

    #LISTS
    print("LISTS")
    list1 = [1, 5, 6, 7, 5, 10]
    print("\nThis is a list: ", list1)

    #add a number to the list
    success = False #incase user doesn't type a number
    while not success:
        try:
            x = input("What number would you like to add to the list? ")
            float(x)
            success = True
        except ValueError:
            print("Please type a number")
    x = float(x)
    list1.append(x)
    print(list1)

    #sum of list
    print("\nYou can also find a sum of a list by typing sum(list1)")
    print(sum(list1))

    #reverse list
    print("\nYou can use the reverse function to switch the order of the list")
    list1.reverse()
    print(list1)

    #other functions
    print("\nRemove an item (1 is removed):")
    list1.remove(1)
    print(list1)
    print("\nCount how many 5:")
    count = list1.count(5)
    print(count, "5s in the list")


    #TUPLES
    print("\n \nTUPLES")
    tup1 = ("a", "c", "d", "f", "a", "e", "a", "f")
    print("\nThis is a tuple: ", tup1)
    print("This difference between a list and a tuple is you can't change the items in a tuple.")

    #count
    print('''\nCount how many a's using tup1.count("a")''')
    count_a = tup1.count("a")
    print(count_a, "a's in the tuple")

    #slicing
    print("You can print a range of items from the tuple by using tup1[1:4] which will print items 2, 3, and 4")
    print(tup1[1:4])
    

if (__name__=="__main__"):
    main()
