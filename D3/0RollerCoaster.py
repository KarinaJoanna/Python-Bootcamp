# Conditional statements
# if / else statements
height = int(input("What is yout heigt  in cm?"))
if height >= 120:
    print("You can ride the rollercoaster")
    # Nested if / else statements
    age = int(input("What is your age?"))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("You can't ride the rollercoaster")