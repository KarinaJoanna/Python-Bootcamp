# Program that tests the compatibility between two people

print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")

#Convert both names to lower case
combined_string = name1.lower() + name2.lower()

#Count the number of times the letters true occurs in the combined string
t = combined_string.count("t")
r = combined_string.count("r")
u = combined_string.count("u")
e = combined_string.count("e")

#Count the number of times the letters love occurs in the combined string
l = combined_string.count("l")
o = combined_string.count("o")
v = combined_string.count("v")
e = combined_string.count("e")

#Add up the true and love counts
true = t + r + u + e
love = l + o + v + e

#Convert the true and love counts to a string
true_love = str(true) + str(love)

#Convert the string to an integer
true_love_int = int(true_love)

#Print the result
if (true_love_int < 10) or (true_love_int > 90):
    print(f"Your score is {true_love_int}, you go together like coke and mentos.")
elif (true_love_int >= 40) and (true_love_int <= 50):
    print(f"Your score is {true_love_int}, you are alright together.")  