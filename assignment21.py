# Sanjana Wadhwani
# 1st Period
# Feb 5th, 2020
# Assignment 21

def main():
    #title
    print("Day of the Week that a Date is on")
    print("=================================")

    #input for date - with error-throwing
    success = False
    while not success: 
        try:
            date = list(map(int, input("\nType the date as MM DD YYYY. For example, Jan 1, 2020 would be 01 01 2020: ").split())) #input for the data set
            success = True
        except ValueError:
            print("Please make sure that you type the date in the correct format and only use numbers")

    #format date from list
    import datetime
    try:
        mon = date[0]
        day = date[1]
        yr = date[2]
        x = datetime.datetime(yr, mon, day) #makes it a date
    except ValueError and IndexError:
        print("The values entered in did not correspond to an actual date. Please try again\n")
        main()

    #print answer
    print(x.strftime("%B"), x.strftime("%d"), ",", x.strftime("%Y"), "is on a", x.strftime("%A"))
    done()


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
