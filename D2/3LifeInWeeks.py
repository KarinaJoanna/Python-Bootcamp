#Round numbers

#print(round(8/3, 2)) # ,2 round to 2 decimal places


#result = 4 / 2
#result /= 2
#print(result)

# f-strings

#score = 0
#height = 1.8
#isWinning = True
#print(f"your score is {score}, your height is {height}, you are winning is {isWinning}")

# Life in Weeks

# 1 year = 365 days
# 1 year = 52 weeks
# 1 year = 12 months

age = input("What is your current age? ")
age_as_int = int(age)
years_remaining = 90 - age_as_int
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12
print(f"You have {days_remaining} days, {weeks_remaining} weeks, and {months_remaining} months left.")