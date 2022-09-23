# Programmer: Izzy Ramirez
# Program: Odd Number
# First created: 9/19/22 8:22:00 CST
# Last changed: 9/22/22 9:11:00 CST
# Version: Python 3.10.6

print("Odd numbers from the first natural hundred numbers")
for i in range(0, 101):
    if (i % 2) != 0:
        print(i, end=" ")
#
# print("Alternate approach")
# for k in range(1, 51):
#     if k == 11 or k == 21 or k == 31 or k == 41:
#         print("\n")
#     print(((2*k)-1), end=" ")
