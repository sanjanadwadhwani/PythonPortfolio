# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 18

#get numbers from user
def main():
    global list1
    success = False
    while not success:
        try:
            list1 = list(map(int, input("Type the numbers you want to do calculations with: ").split())) #input for the data set
            success = True
        except ValueError:
            print("Error. Please type numbers and separate the numberss by spaces.")
    print(list1)
    dict1 = calculations(list1)
    list1.sort()

    #output
    print("\nYour list sorted: ", list1)
    print('The median is', dict1['median'])
    print('The mean is', dict1['mean'])
    print('The mode is', dict1['mode'])
    print('The range is', dict1['range'])
    print('The MAD is', dict1['MAD'])

    #again
    done()

#start calculations
def calculations(x):
    from stats import median, mean, mode, MAD, RANGE
    return {'median': median(x), 'mean': mean(x), 'mode': mode(x), 'range': RANGE(x), 'MAD': MAD(x)}


#when finished
def done():
    done = str(input("\nDo you want to try again? "))
    if (done.upper() != "YES" and done.upper() != "NO"):
        while done.upper() != "YES" and done.upper() != "NO":
            done = str(input("Please type yes or no: "))
            if done.upper() == "YES" or done.upper() == "NO":
                break
    if (done.upper() == "YES"):
        print("")
        main()
    if (done.upper() == "NO"):
        exit()

    
if (__name__=="__main__"):
    main()
