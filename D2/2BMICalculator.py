#Addition 3 + 5
#Subtraction 7 - 4
#Multiplication 3 * 2
#Division 6 / 3
#Exponent 3 ** 2

#PEMDASLR
#Parentheses    ()
#Exponents      **
#Multiplication *
#Division       /
#Addition       +
#Subtraction    -

#BMI Calculator

height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")

bmi = float(weight) / float(height) ** 2
print(int(bmi))