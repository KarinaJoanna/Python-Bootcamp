import random
import my_module

random_integer = random.randint(1, 10)
print(random_integer)

# Path: D4/my_module.py
print(my_module.pi)

#0.00000 - 0.99999...
random_float = random.random() 
print(random_float)

#0.00000 - 4.99999...
random_float = random.random() * 5
print(random_float)

love_score = random.randint(1, 100)
print(f"Your love score is {love_score}")