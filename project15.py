# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 15


def main():
    print("Hello!")
    global list1
    list1 = list(map(int, input("\nType the numbers you want to do calculations with: ").split())) #input for the data set
    print(list1)
    calculations()



#which calculation to do
def calculations():
    operation = input("\nMax, Min, Median, Mode, or Mean: ") #which operation to use
    global oper
    oper = str(operation) #makes input a string
    from refermod import maximum, minimum, median, mean, mode 
    
    #max
    if (oper.upper() == 'MAX'):
        z = maximum(list1)
        print("The max is", z)
        restart()

    #min
    if (oper.upper() == 'MIN'):
        z = minimum(list1)
        print("The min is", z)
        restart()

    #median
    if (oper.upper() == 'MEDIAN'):
        z = median(list1)
        print("The median is", z)
        restart()

    #mean
    if (oper.upper() == 'MEAN'):
        z = mean(list1)
        print("The mean is", z)
        restart()

    #mean
    if (oper.upper() == 'MODE'):
        z = mode(list1)
        print("The mode is", z)
        restart()




    #if user did not type in any of the operations correctly
    else:
        print("Please either type max, min, mode, median, or mean")
        calculations()




#defining the operation functions
def maximum(x):
    return max(x)

def minimum(x):
    return min(x)

def median(x):
    import statistics
    return statistics.median(x)

def mean(x):
    import statistics
    return statistics.mean(x)

def mode(x):
    import statistics
    try:
        y = statistics.mode(x)
        return statistics.mode(x)
    except ValueError:
        return "N/A"




def restart():

    #new calculation
    restart = str(input("\nWould you like to do another calculation? "))

    #user did not type yes or no
    if (restart.upper() != "NO" and restart.upper() != "YES"):
        while restart.upper() != "NO" or "YES":
            restart = str(input("Please type yes or no. Would you like to do another calculation? "))
            if restart.upper() == "NO" or "YES":
                break
            
    #restart
    if (restart.upper() == "YES"):
        new = str(input("Do you have a new set of numbers? "))
        if new.upper() == "YES": #new set of numbers
            main()
        if new.upper() == "NO": #same set of numbers
            print("")
            print(list1)
            calculations()
        if new.upper() != "NO" or "YES": #user did not type yes or no
            while restart.upper() != "NO" or "YES":
                restart = str(input("Please type yes or no. Would you like to do another calculation? "))
                if restart.upper() == "NO" or "YES":
                    break
    #end      
    if (restart.upper() == "NO"):
        print("Okay, bye!")
        exit()

    
    

if (__name__=="__main__"):
    main()
