# Sanjana Wadhwani
# 1st Period
# January 14, 2020
# Assignment 6

#intro
def main():
    print("Temperature Conversions \n")
    print("Here are the formulas: \n")
    print("Kelvin to Farhenheit: F = [ (9 * (K - 273)) / 5 ] + 32.")
    print("Kelvin to Celsius: C = K - 273.")
    print("Farhenheit to Celsius: C = [ (F - 32) * 5 ] / 9.")
    print("Farhenheit to Kelvin: K = [ ((F - 32) * 5) ] / 9 ] + 273.")
    print("Celsius to Farhenheit: F = [(9 * C) / 5 ] + 32.")
    print("Celsius to Kelvin: K = C - 273\n")
    conversions()
    

#start the actual conversion
def conversions():
    start = str(input("What are you starting with? Farhenheit (F), Celsius (C), or Kelvin (K)? "))

    #if user did not type it in correctly
    if (start.upper() != "KELVIN" and start.upper() != "K" and start.upper() != "CELSIUS" and start.upper() != "C" and start.upper() != "FARHENHEIT" and start.upper() != "F"):
        while (start.upper() != "KELVIN" and start.upper() != "K" and start.upper() != "CELSIUS" and start.upper() != "C" and start.upper() != "FARHENHEIT" and start.upper() != "F"):
            start = str(input("Please either type kelvin, k, celsius, c, farhenheit, or f: "))
            if (start.upper() == "KELVIN" or start.upper() == "K" or start.upper() == "CELSIUS" or start.upper() == "C" or start.upper() == "FARHENHEIT" or start.upper() == "F"):
                break

    if (start.upper() == "KELVIN" or start.upper() == "K"): #starting with Kelvin
        kelvin()
    if (start.upper() == "CELSIUS" or start.upper() == "C"): #starting with Celsius
        celsius()
    if (start.upper() == "FARHENHEIT" or start.upper() == "F"): #starting with Farhenheit
        farhenheit()



#if you are starting with Kelvin
def kelvin():
    
    #asks for how much Kelvin and prevents errors if user doesn't type in a number
    success = False
    while not success:
        try:
            K = input("\nWhat is the temperature in Kelvin? ")
            float(K)
            success = True
        except ValueError:
            print("Please type a number")
            kelvin()
    K = float(K)

    end_unit = str(input("What do you want? Farhenheit (F) or Celsius (C)? ")) #as what to convert it to 

    #if user did not type it in correctly
    if (end_unit.upper() != "CELSIUS" and end_unit.upper() != "C" and end_unit.upper() != "FARHENHEIT" and end_unit.upper() != "F"):
        while (end_unit.upper() != "CELSIUS" and end_unit.upper() != "C" and end_unit.upper() != "FARHENHEIT" and end_unit.upper() != "F"):
            end_unit = str(input("Please either type celsius, c, farhenheit, or f: "))
            if (end_unit.upper() == "CELSIUS" or end_unit.upper() == "C" or end_unit.upper() == "FARHENHEIT" or end_unit.upper() == "F"):
                break

    #convert K to F
    if (end_unit.upper() == "FARHENHEIT" or end_unit.upper() == "F"):
        F = ((9 * (K - 273))/5) + 32
        print("")
        print(K, "Kelvin is equal to", F, "degrees Farhenheit")
        done()

    #convert K to C
    if (end_unit.upper() == "CELSIUS" or end_unit.upper() == "C"):
        C = K - 273
        print("")
        print(K, "Kelvin is equal to", C, "degrees Celsius")
        done()




#if you are starting with celsius
def celsius():

    #asks for how much celsius and prevents errors if user doesn't type in a number
    success = False
    while not success:
        try:
            C = input("\nWhat is the temperature in Celsius? ")
            float(C)
            success = True
        except ValueError:
            print("Please type a number")
            celsius()
    C = float(C)

    end_unit = str(input("What do you want? Farhenheit (F) or Kelvin (K)? ")) #asks what to convert it to

    #if user did not type it in correctly 
    if (end_unit.upper() != "KELVIN" and end_unit.upper() != "K" and end_unit.upper() != "FARHENHEIT" and end_unit.upper() != "F"):
        while (end_unit.upper() != "KELVIN" and end_unit.upper() != "K" and end_unit.upper() != "FARHENHEIT" and end_unit.upper() != "F"):
            end_unit = str(input("Please either type kelvin, k, farhenheit, or f: "))
            if (end_unit.upper() == "KELVIN" or end_unit.upper() == "K" or end_unit.upper() == "FARHENHEIT" or end_unit.upper() == "F"):
                break

    #convert C to F
    if (end_unit.upper() == "FARHENHEIT" or end_unit.upper() == "F"):
        F = ((9 * C)/5) + 32
        print("")
        print(C, "degrees Celsius is equal to", F, "degrees Farhenheit")
        done()

    #convert C to K
    if (end_unit.upper() == "KELVIN" or end_unit.upper() == "K"):
        C = K - 273
        print("")
        print(C, "degrees Celsius is equal to", K, "Kelvin")
        done()



#if you are starting with farhenheit
def farhenheit():

    #asks for how much Kelvin and prevents errors if user doesn't type in a number
    success = False
    while not success:
        try:
            F = input("\nWhat is the temperature in Farhenheit? ")
            float(F)
            success = True
        except ValueError:
            print("Please type a number")
            farhenheit()
    F = float(F)

    end_unit = str(input("What do you want? Celsius (C) or Kelvin (K)? ")) #asks what to convert it to

    #if user did not type it in correctly 
    if (end_unit.upper() != "KELVIN" and end_unit.upper() != "K" and end_unit.upper() != "CELSIUS" and end_unit.upper() != "C"):
        while (end_unit.upper() != "KELVIN" and end_unit.upper() != "K" and end_unit.upper() != "CELSIUS" and end_unit.upper() != "C"):
            end_unit = str(input("Please either type kelvin, k, celsius, or c: "))
            if (end_unit.upper() == "KELVIN" or end_unit.upper() == "K" or end_unit.upper() == "CELSIUS" or end_unit.upper() == "C"):
                break

    #convert C to F
    if (end_unit.upper() == "CELSIUS" or end_unit.upper() == "C"):
        C = ((F - 32) *5)/9
        print("")
        print(F, "degrees Farhenheit is equal to", C, "degrees Celsius")
        done()

    #convert C to K
    if (end_unit.upper() == "KELVIN" or end_unit.upper() == "K"):
        C = K - 273
        print("")
        print(C, "degrees Celsius is equal to", K, "Kelvin")
        done()


#after conversion is completed
def done():
    done = str(input("\nDo you want to do another conversion? "))
    if (done.upper() != "YES" and done.upper() != "NO"):
        while (done.upper() != "YES" and done.upper() != "NO"):
            done = str(input("Please type yes or no: "))
            if (done.upper() == "YES" or done.upper() == "NO"):
                break
    if (done.upper() == "YES"):
        conversions()
    if (done.upper() == "NO"):
        exit()
    


if (__name__=="__main__"):
    main()

