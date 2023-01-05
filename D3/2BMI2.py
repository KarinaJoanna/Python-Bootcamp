#BMI Calculator v 2.0

#Get the height
height = float(input("Enter your height in m: "))
#Get the weight
weight = float(input("Enter your weight in kg: "))
#Calculate the BMI
bmi = round(weight / height ** 2)
# Conditional statements
if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are clinically obese.")