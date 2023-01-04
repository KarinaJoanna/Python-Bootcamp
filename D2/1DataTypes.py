#Data Types

#String 
# print("Hello"[4])

#Integer 
# print(123 + 345)

#Float 
# print(3.14159)

#Boolean
#True
# False

two_digit_numer = input("2 digit number")
#print(type(two_digit_numer))
first_digit = two_digit_numer[0]
second_digit = two_digit_numer[1]
#we have to convert the string to integer
result = int(first_digit) + int(second_digit)
print(result)
