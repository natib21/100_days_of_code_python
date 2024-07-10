print("Welcome To Python Pizza Delivery")
size = input("What Size pizza do you want ? S , M or H .")
add_pepperoni = input("Do you Want Pepperoni ? Y or N .")
extra_cheese = input("Do you Want Extra Cheese ? Y or N .")
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_medium_or_large = 3
cheese = 1

bill = 0
if size == 'S':
    bill = small_pizza
    if add_pepperoni == 'Y':
        bill += pepperoni_small
    if extra_cheese == 'Y':
        bill += cheese   
        print(f"Your final bill is: {bill}")
    else:
         print(f"Your final bill is: {bill}")  
elif size == 'M':
    bill = medium_pizza
    if add_pepperoni == 'Y':
        bill += pepperoni_medium_or_large
    if extra_cheese == 'Y':
        bill += cheese   
        print(f"Your final bill is: {bill}")
    else:
         print(f"Your final bill is: {bill}")  
elif size == 'H':
    bill = large_pizza
    if add_pepperoni == 'Y':
        bill += pepperoni_medium_or_large
    if extra_cheese == 'Y':
        bill += cheese   
        print(f"Your final bill is: {bill}")
    else:
         print(f"Your final bill is: {bill}") 
else :
    print("Pls Enter The Valid Letters ")