'''
Name: Robert Jones
Date: 8/26/2024
Purpose: The purpose of this program is to display ineffective use of input validation.
Version: 1.0
'''

# Prompt isn't clarifying what numbers are for.
print("Pick two numbers.")

# No line breaks commands will looked jumbled.
num1 = int(input("First Number"))
num2 = int(input("Second Number"))
newNumber = num1 + num2

# Output doesn't clarify what the user can expect.
print(newNumber)


