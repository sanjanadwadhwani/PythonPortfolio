# Sanjana Wadhwani
# 1st Period
# Feb 19, 2020
# Assignment 28

#get numbers from user
def main():
    global list1
    success = False
    while not success:
        try:
            list1 = list(map(int, input("Type the numbers you want to do calculations with: ").split())) #input for the data set
            success = True
        except ValueError:
            print("Error. Please type numbers and separate the numbers by spaces.")
    print(list1)
    dict1 = calculations(list1)
    list1.sort()

    #output
    print("\nYour list sorted: ", list1)
    print('The median is', dict1['median'])
    print('The mean is', dict1['mean'])
    print('The mode is', dict1['mode'])
    print('The range is', dict1['range'])
    print('The maximum is', dict1['max'])
    print('The minimum is', dict1['min'])

    #again
    done()

#start calculations
def calculations(x):
    rang = lambda y, z: y - z
    y = max(x)
    z = min(x)
    from stats import median, mode
    return {'median': median(x), 'mean': avg(x), 'mode': mode(x), 'range': rang(y, z), 'max': y, 'min': z}


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

def avg(x):
    return sum(x) / len(x)

    
if (__name__=="__main__"):
    main()
