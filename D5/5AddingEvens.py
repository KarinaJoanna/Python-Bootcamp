# Adding Evens

total = 0
for number in range(2, 101, 2): #Start at 2, go up to 100, and goes up by 2
    total += number
print(total)
    
total2 = 0
for number in range(1, 101):
    if number % 2 == 0:
        total2 += number
print(total2)