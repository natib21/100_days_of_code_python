year = int(input("Which Year do You Want To check ? "))
if year % 4 == 0 :
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap Year")
        else:
            print("No Leap Year")    
else:
    print("No Leap Year")
        