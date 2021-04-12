"""
Plain English
Start

Create a list to store five numbers (Float)
Capture User's input five times for their grades
Each time we capture the User's input, we append the number to the list

Sort the list ascending, then splice the items starting at index 2

Once we have three highest number in the list, we sum them up and 
divide by 3

Output a message to the User

End
"""
"""
Pseudocode


Create List1

Capture Input
Append number to list

Capture Input
Append number to list

Capture Input
Append number to list

Capture Input
Append number to list

Capture Input
Append number to list

Sort the list and splice out the lowest number

Print Message to User
"""

grades = []

grade = input("Enter the 1st grade: ")
grades.append(float(grade))

grade = input("Enter the 2nd grade: ")
grades.append(float(grade))

grade = input("Enter the 3rd grade: ")
grades.append(float(grade))

grade = input("Enter the 4th grade: ")
grades.append(float(grade))

grade = input("Enter the 5th grade: ")
grades.append(float(grade))

grades.sort()

grades = grades[2:]

grades = sum(grades)

result = grades/3

print("Average Grade {0:.2f}%".format(result))
