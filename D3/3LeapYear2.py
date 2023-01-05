# Leap Year
# This program determines if a year is a leap year

print("Leap Year")
#Get the year
year = int(input("Enter a year: "))
#Check if the year is a leap year
if year % 4 == 0:
    print("Leap year")
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year")
        else:
            print("Not leap year")
    else:
        print("Leap year")
else:
    print("Not leap year")