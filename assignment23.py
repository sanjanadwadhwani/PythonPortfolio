# Sanjana Wadhwani
# 1st Period
# Feb 5th, 2020
# Assignment 23

def main():

    #create the file
    print('First use f = open("test.py", "a") to create a file')
    f = open("test.py", "a")

    #add more content to the file
    print("Use f.write() to add more text to the file")
    f.write("Use f.write() to add more text to the file\n")

    
    #loop for adding text from input
    success = False
    while (not success):
        try:
            num = int(input("How many lines do you want to add? "))
            success = True
        except ValueError:
            print("You need to type a number.")
    for i in range(num):
        f.write("This is a line %d\r\n" % (i+1))

    #print file content
    print('\nThis is what is on the file right now')
    f = open("test.py", "r")
    print(f.read())

    

if (__name__=="__main__"):
    main()
