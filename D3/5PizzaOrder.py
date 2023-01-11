print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L \n")
add_pepperoni = input("Do you want pepperoni? Y or N \n")
extra_cheese = input("Do you want extra cheese? Y or N \n")

bill = 0
small_pizza = 15
medium_pizza = 20
large_pizza = 25
pepperoni_small = 2
pepperoni_medium_large = 3

if size == "S":
    bill += small_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_small
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

if size == "M":
    bill += medium_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")

if size == "L":
    bill += large_pizza
    if add_pepperoni == "Y":
        bill += pepperoni_medium_large
        if extra_cheese == "Y":
            bill += 1
            print(f"Your final bill is ${bill}")
        else:
            print(f"Your final bill is ${bill}")
    else:
        print(f"Your final bill is ${bill}")