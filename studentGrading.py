#Programmer: Izzy Ramirez
#Program: Student Grading
#First created: 9/16/2022 9:20 CST
#Last changed: 9/16/22 10:42 CST
#Version: Python 3.10.6

print("Welcome to Grade Assignment \n")
name = str(input("Please enter your name: \n"))
SCID = str(input("Please enter your ID number: \n"))
assign = int(input("Please enter your assignment percentage: \n"))
lab = int(input("Please enter your lab percentage: \n"))
read = int(input("Please enter your reading and participation percentage: \n"))
quiz = int(input("Please enter your quiz percentage: \n"))
mid = int(input("Please enter your midterm percentage: \n"))
project = int(input("Please enter your project percentage: \n"))
total = int(assign + lab + read + quiz + mid + project)

if total >= 94:
    print("Letter grade: A \n")
    print("GPA: 4.00 \n")
    print("Excellent performance")
elif total >= 90:
    print("Letter grade: A- \n")
    print("GPA: 3.67 \n")
    print("Excellent performance")
elif total >= 87:
    print("Letter grade: B+ \n")
    print("GPA: 3.33 \n")
    print("Good performance")
elif total >= 84:
    print("Letter grade: B \n")
    print("GPA: 3.00 \n")
    print("Good performance")
elif total >= 80:
    print("Letter grade: B- \n")
    print("GPA: 2.67 \n")
    print("Good performance")
elif total >= 77:
    print("Letter grade: C+ \n")
    print("GPA: 2.33 \n")
    print("Average performance")
elif total >= 74:
    print("Letter grade: C \n")
    print("GPA: 2.00 \n")
    print("Average performance")
elif total >= 70:
    print("Letter grade: C- \n")
    print("GPA: 1.67 \n")
    print("Average performance")
elif total >= 65:
    print("Letter grade: D+ \n")
    print("GPA: 1.33 \n")
    print("Unsatisfactory performance")
elif total >= 60:
    print("Letter grade: D \n")
    print("GPA: 1.0 \n")
    print("Unsatisfactory performance")
elif total >= 55:
    print("Letter grade: D- \n")
    print("GPA: 0.67 \n")
    print("Unsatisfactory performance")
else:
    print("letter grade: F \n")
    print("GPA: 0.00 \n")
    print("Failing performance")
