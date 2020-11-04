# Sanjana Wadhwani
# 1st Period
# Feb 5th, 2020
# Assignment 20

def main():
    shape = input("Do you have a sphere (A), cube (B), cylinder (C), or rectangular prism (D)? ")
    from volume import sphere, cube, cyl, rect

    if (shape.upper() != "A" and shape.upper() != "B" and shape.upper() != "C" and shape.upper() != "D"): #errors
        while (shape.upper() != "A" and shape.upper() != "B" and shape.upper() != "C" and shape.upper() != "D"):
            print("Please type A, B, C, or D")
            shape = input("Do you have a sphere (A), cube (B), cylinder (C), or rectangular prism (D)? ")
            if (shape.upper() == "A" and shape.upper() == "B" and shape.upper() == "C" and shape.upper() == "D"):
                break

    if (shape.upper() == "A"): # if sphere
        print("\nTHE VOLUME OF A SPHERE")
        print("======================")
        varisphere()
        ans = sphere(r) #find volume of a sphere
        print("\nThe volume of the sphere with radius", r, "is", ans)

    if (shape.upper() == "B"): # if cube
        print("\nTHE VOLUME OF A CUBE")
        print("======================")
        varicube()
        ans = cube(s) #find volume of a cube
        print("\nThe volume of the cube with side length", s, "is", ans)

    if (shape.upper() == "C"): # if cylinder
        print("\nTHE VOLUME OF A CYLINDER")
        print("======================")
        varicyl()
        ans = cyl(r, h) #find volume of a cylinder
        print("\nThe volume of the cylinder with radius", r, "and height", h, "is", ans)

    if (shape.upper() == "D"): # if rectangular prism
        print("\nTHE VOLUME OF A RECTANGULAR PRISM")
        print("======================")
        varirect()
        ans = rect(l, w, h) #find volume of a cylinder
        print("\nThe volume of the cylinder with length", l, "width", w, "and height", h, "is", ans)

    done()




#define variables for volume of a sphere         
def varisphere():
    success = False
    while not success:
        try:
            global r
            r = float(input("Please type the radius: "))
            success = True
        except ValueError:
            print("Error. Type a number.")


#define variables for volume of a cube
def varicube():
    success = False
    while not success:
        try:
            global s
            s = float(input("Please type the side length: "))
            success = True
        except ValueError:
            print("Error. Type a number.")


#define variables for volume of a cylinder
def varicyl():
    success = False
    while not success:
        try:
            global s
            s = float(input("Please type the side length: "))
            success = True
        except ValueError:
            print("Error. Type a number.")


#define variables for volume of a cube
def varicyl():
    success = False
    while not success:
        try:
            global r, h
            r = float(input("Please type the radius: "))
            h = float(input("Please type the height: "))
            success = True
        except ValueError:
            print("Error. Type a number.")

#define variables for volume of a rectangular prism
def varirect():
    success = False
    while not success:
        try:
            global l, w, h
            l = float(input("Please type the length: "))
            w = float(input("Please type the width: "))
            h = float(input("Please type the height: "))
            success = True
        except ValueError:
            print("Error. Type a number.")

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
