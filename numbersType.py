# Programmer: Izzy Ramirez
# Program: Numbers Type
# First Created: 9/26/22 8:03:00 CST
# Last Edited: 9/26/22 8:46:00 CST
# Version: 1.0.0

# odd numbers
print("Odd numbers from the first hundred natural numbers")
for i in range(0, 100):
    if (i % 2) != 0:
        print(i, end=" ")

# even numbers
print("\nEven numbers from the first hundred natural numbers")
for i in range(0, 100):
    if (i % 2) == 0:
        print(i, end=" ")

# prime numbers
print("\nPrime numbers from the first hundred natural numbers")
counter = 0         # initializing counter variable to 0
for n in range(1, 101):
    for i in range(2, int((n / 2) + 1)):  # iterating for numbers between 2 and n/2 + 1
        # checking number of divisors for a number
        if n % i == 0:          # check for remainder is 0
            counter = counter + 1       # increase counter if you find a divisor
    if counter == 0:            # decision to see if counter is 0
        print(n, end=" ")       # printing if number is prime
    counter = 0

# perfect numbers
print("\nPerfect numbers from the first hundred natural numbers")
sum = 0
check = 0
for n in range(1, 101):
    for i in range(1, int((n / 2) + 1)):
        check = int(n % i)
        if check == 0:
            sum = int(sum + i)
    if n == sum:
        print(n, end=" ")
    sum = 0
# palindrome numbers
# print("\nPalindrome numbers from the first hundred natural numbers")
