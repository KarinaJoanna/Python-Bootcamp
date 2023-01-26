# Prime Number Checker

# Prime numbers are numbers that have only two factors - 1 and the number itself.

def prime_checker(number):
    is_prime = True
    for i in range(2, number): 
        # i is the number we are checking if it is a factor of number
        # range start at 2 because 1 is a factor of every number
        if number % i == 0:
            is_prime = False
    if is_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")

n = int(input("Check this number: "))
prime_checker(number=n)