import random

# Split string method
names_string = input("Give me everybody's names, separated by a comma.\n ")
names = names_string.split(", ")

random_name = random.choice(names)
print(f"{random_name} is going to buy the meal today!")