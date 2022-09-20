#Programmer: Izzy Ramirez
#Program: Loops
#First created: 9/19/22 8:22:00 CST
#Last changed: 9/19/22 8:43:00 CST
#Version: Python 3.10.6

print("Odd numbers from the first natural hundred numbers")
for i in range(0, 101):
    if (i % 2) != 0:
        print(i, end=" ")
