print ("Hello User. Thank you for using our programme. We will help you convert kilometers into miles.")

odgovor="y"
while odgovor=="y":
    number_of_km=int(input ("Please enter the number of kilometers: "))
    number_of_miles=float(number_of_km/1.61)
    print(str(number_of_km)+" kilometers is "+str(number_of_miles)+" miles")
    odgovor=input ("Would you like to do another conversion? (y/n) ").lower()
    if odgovor=="n":
        break









