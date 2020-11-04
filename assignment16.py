# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 16


def main():
    print("Hello!")
    global list1
    list1 = list(map(int, input("\nType the numbers you want to find the mean absolute deviation of: ").split())) #input for the data set
    print("The data set is", list1)
    mad = MAD(list1) #finds mean absolute deviation
    print("\nThe mean absolute deviation is", mad)

#returns mean absolute deviation
def MAD(x):
    m = mean(x)
    list2 = []
    for i in range(len(x)):
        dev = abs(x[i] - m)
        list2.append(dev)
    return mean(list2)
        
#returns mean of data set inputed
def mean(x):
    return sum(x)/len(x)



if (__name__=="__main__"):
    main()
