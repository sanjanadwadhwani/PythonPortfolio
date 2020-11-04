# Sanjana Wadhwani
# 1st Period
# Feb 5, 2020
# Statistics

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

def RANGE(x):
    largest = x[len(x)-1]
    smallest = x[0]
    return largest - smallest

def MAD(x):
    m = mean(x)
    list2 = []
    for i in range(len(x)):
        dev = abs(x[i] - m)
        list2.append(dev)
    return mean(list2)
        
