"""
Programmer: Izzy Ramirez
Program: Numbers Type
First Created: 9/26/22 8:03:00 CST
Last Edited: 10/14/22 8:54:00 CST
Version: 2.1.0

"""
print("Welcome to mathematical operations.")
print("1: Odd Numbers\n"
      "2: Even Numbers\n"
      "3: Prime Numbers\n"
      "4: Perfect Numbers\n"
      "5: Palindrome Numbers")
choice = int(input("\nSelect desired operation by entering a number: "))


# odd numbers
def odd_numbers(lowerBound, upperBound):
    print("\nOdd numbers from the first hundred natural numbers")
    for i in range(lowerBound, upperBound):
        if (i % 2) != 0:
            print(i, end=" ")


# even numbers
def even_numbers(lowerBound, upperBound):
    print("\nEven numbers from the first hundred natural numbers")
    for i in range(lowerBound, upperBound):
        if (i % 2) == 0:
            print(i, end=" ")


# prime numbers
def prime_numbers(lowerBound, upperBound):
    print("\nPrime numbers from the first hundred natural numbers")
    counter = 0         # initializing counter variable to 0
    for n in range(lowerBound, upperBound):
        for i in range(2, int((n / 2) + 1)):  # iterating for numbers between 2 and n/2 + 1
            # checking number of divisors for a number
            if n % i == 0:          # check for remainder is 0
                counter = counter + 1       # increase counter if you find a divisor
        if counter == 0:            # decision to see if counter is 0
            print(n, end=" ")       # printing if number is prime
        counter = 0


# perfect numbers
def perfect_numbers(lowerBound, upperBound):
    print("\nPerfect numbers from the first hundred natural numbers")
    sum = 0
    check = 0
    for n in range(lowerBound, upperBound):
        for i in range(1, int((n / 2) + 1)):
            check = int(n % i)
            if check == 0:
                sum = int(sum + i)
        if n == sum:
            print(n, end=" ")
        sum = 0


# palindrome numbers
def palindrome_numbers(lowerBound, upperBound):
    print("\nPalindrome numbers from the first hundred natural numbers")
    for number in range(lowerBound, upperBound):
        originalNumber = number
        reverse = 0
        while number > 0:
            remainder = int(number % 10)
            reverse = int(reverse * 10 + remainder)
            number = int(number / 10)
        if originalNumber == reverse:
            print(originalNumber, end=" ")


match choice:
    case 1:
        odd_numbers(0, 100)
    case 2:
        even_numbers(200, 400)
    case 3:
        prime_numbers(0, 100)
    case 4:
        perfect_numbers(0, 100)
    case 5:
        palindrome_numbers(0, 100)
