# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 11

def main():

    #SETS
    print("SETS")
    print("A set is an unordered collection of items. There are no duplicates in a set.")

    #set of integers
    set1 = {3, 5, 7, 8, 7}
    print("\nThis is a set of integers: ", set1, "Any duplicate items are not shown twice when the set it printed.")

    #adding items to set
    success = False #incase user doesn't type a number
    while not success:
        try:
            x = input("\nWhat would you like to add to the set (Don't use a number already in the set): ")
            float(x)
            success = True
        except ValueError:
            print("Please type a number")
    x = float(x)
    print("You can add something to the set by using set1.add(x)")
    set1.add(x)
    print(set1)
    print("\nYou can add multiply items at once by using set1.update([2,3,6])")
    set1.update([2, 4, 6])
    print(set1)

    #removing items from a set
    print("\nTo remove items, you can use remove() or discard(). Remove() will raise an error if the item does not exist by discard will not.")
    print("For example, I will remove 7 from the list by using set1.discard(7)")
    set1.discard(7)
    print(set1)

    #set unions and differences
    print("\nYou can find the items that are the same or different in two sets.")
    print("Your first set is", set1)
    set2 = {5, 7, 9, 10, 32, 2}
    print("Your second set is", set2)
    print("\nUsing print(set1 | set2), you can print all the items in set 1 and 2.")
    print(set1 | set2)
    print("\nUsing print(set1 & set2), you can print all the items in common between the two sets.")
    print(set1 & set2)
    print("\nUsing print(set1 - set2), you can print all the items not in common between the two sets.")
    print(set1 - set2)


    #DICTIONARIES
    print("\n\nDICTIONARIES")
    print("A dictionary in python is an unordered collection of items that has a key")

    #dictionary of words
    dict1 = {1: 'dog', 2: 'cat', 3: 'bird', 4: 'hamster'}
    print("\nThis is an example of a dictionary: ", dict1)

    #accessing elements
    print("\nWhen trying to get an element, you use the key. You can either use print(my_dict[1]) or print(my_dict.get(1)). Using get() will avoid a key error because it will print none")
    print("For example, if I use print(dict1.get(1)), it will print dog, but if I use print(dict1.get(7)), it will print none.")
    print("")
    print(dict1.get(1))
    print(dict1.get(7))

    #adding items
    print("\nTo add items, you use dict1[5] = 'fish'")
    dict1[5] = 'fish'
    print(dict1)

    #removing items
    print("\nTo remove items, you use dict1.pop(1).")
    dict1.pop(1)
    print(dict1)
    print("\nTo remove a random item, you can use dict1.popitem()")
    dict1.popitem()
    print(dict1)
    

if (__name__=="__main__"):
    main()
