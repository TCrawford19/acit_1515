"""
1. Given the 'grade' variable below, write a conditional statement that outputs 'You passed!' 
if the entered value is greater than 50, or 'Sorry, try again!' if the value is lower than 50
"""
grade = input('Please enter a grade: ')

"""
2. Fix the statements below such that "Thank you for entering a value" is only output if the user enters a value
"""
name = input('Please enter your name: ')
if name == "":
    print('You did not enter a value')
else:
    print(f'Hello {name}')

print('Thank you for entering a value')

"""
3. Combine the following conditional statements into a single if/else block
"""
age = 16
if age > 16:
    print('You can drive')
if age < 16:
    print('You cannot drive')

"""
4. Combine the following three if statements into an if/elif/else block
"""
if age < 18:
    print('You are too young to work')
if age > 65:
    print('You are too old to work')
if age > 18 and age < 65:
    print('You are the right age to work')

"""
5. Combine the following conditional statements into a single conditional statement using 'and', 
with the following caveat:

    In order to pass the course, you must make effort, and hand in assignments, and read instructions

Add an else block to indicate the case where you will not pass the course.
"""
makeEffort = True
handInAssignments = True
readInstructions = True

if makeEffort:
    print('You will pass the course')
else:
    print('You will fail the course')
if handInAssignments:
    print('You will pass the course')
else:
    print('You will fail the course')
if readInstructions:
    print('You will pass the course')
else:
    print('You will fail the course')

"""
6. Using the variables from the previous questions, write a single conditional statement using only 'or', with
the same logic as above (i.e. if you don't make effort, read instructions, or hand in assignments you will fail the course)
"""
