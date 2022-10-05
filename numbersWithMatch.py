"""
Programmer: Izzy Ramirez
Program: Numbers Type
First Created: 9/26/22 8:03:00 CST
Last Edited: 9/30/22 10:08:00 CST
Version: 1.0.0

"""
print("Welcome to mathematical operations.")
print("1: Odd Numbers\n"
      "2: Even Numbers\n"
      "3: Prime Numbers\n"
      "4: Perfect Numbers\n"
      "5: Palindrome Numbers")
choice = int(input("\nSelect desired operation by entering a number: "))


# odd numbers
# if choice == 1:
def odd_numbers():
    print("\nOdd numbers from the first hundred natural numbers")
    for i in range(0, 100):
        if (i % 2) != 0:
            print(i, end=" ")

    # odd_numbers()


# even numbers
# elif choice == 2:
def even_numbers():
    print("\nEven numbers from the first hundred natural numbers")
    for i in range(0, 100):
        if (i % 2) == 0:
            print(i, end=" ")

    # even_numbers()


# prime numbers
# elif choice == 3:
def prime_numbers():
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

    # prime_numbers()


# perfect numbers
# elif choice == 4:
def perfect_numbers():
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

    # perfect_numbers()


# palindrome numbers
# elif choice == 5:
def palindrome_numbers():
    print("\nPalindrome numbers from the first hundred natural numbers")
    # reverse = 0
    #number = 121
    for number in range(1, 101):
        originalNumber = number
        reverse = 0
        while number > 0:
            remainder = int(number % 10)
            reverse = int(reverse * 10 + remainder)
            number = int(number / 10)
            # print(reverse)
        if originalNumber == reverse:
            print(originalNumber, end=" ")

    # palindrome_numbers()

# else:
# print("Enter a valid number.")


match choice:
    case 1:
        odd_numbers()
    case 2:
        even_numbers()
    case 3:
        prime_numbers()
    case 4:
        perfect_numbers()
    case 5:
        palindrome_numbers()

