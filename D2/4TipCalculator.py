#Tip calculator
#If the bill is $150.00, split between 5 people, with 12% tip. Each person should pay (150.00 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

print("Welcome to the Tip Calculator")
#Get the bill amount
bill = float(input("Enter the bill amount: $"))
#Get the tip percentage
porcentage_tip = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
#Get the number of people
people = int(input("How many people to split the bill? "))

#Calculate the tip
tip = bill * porcentage_tip / 100
#Calculate the total bill
total_bill = bill + tip
#Calculate the amount per person
amount_per_person = total_bill / people
#Round the amount per person
amount_per_person = round(amount_per_person, 2)
#Print the amount per person
print(f"Each person should pay: ${amount_per_person}")