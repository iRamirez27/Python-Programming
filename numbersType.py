# Programmer: Izzy Ramirez
# Program: Numbers Type
# First Created: 9/26/22 8:03:00 CST
# Last Edited: 9/26/22 8:05:00 CST
# Version: 1.0.0
"""
# odd numbers
print("Odd numbers from the first natural hundred numbers")
for i in range(0, 100):
    if (i % 2) != 0:
        print(i, end=" ")

# even numbers
print("\nEven numbers from the first natural hundred numbers")
for i in range(0, 100):
    if (i % 2) == 0:
        print(i, end=" ")

# prime numbers"""
print("\nPrime numbers from the first natural hundred numbers")
counter = 0
for n in range(1, 101):
    for i in range(2, int((n / 2) + 1)):
        if n % i == 0:
            counter = counter + 1
    if counter == 0:
        print(n, end=" ")
    counter = counter + 1
# perfect numbers

# palindrome numbers
