print('Welcome to the tip calculator')
Total_bill = float(input("What was the total bill ? $"))
tip = int(input("What percentage tip would you like to give? 10 , 12 , or 15 ?"))
people = int(input("how many people to split the bill ?"))

tip_as_percent = tip /100 
total_bill_amount = Total_bill * tip_as_percent
total_bil = Total_bill + total_bill_amount
bill_per_person = total_bil / people 
amount = "{:.2f}".format(bill_per_person)
print(f'Each person should pay: ${amount}')