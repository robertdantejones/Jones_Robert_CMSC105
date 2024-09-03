'''
Name: Robert Jones
Date: 8/26/2024
Purpose: The purpose of this program is to display effective use of input validation.
Version: 1.0
'''

# Prompt clarifies what program is for.
print("Pick two number to perform addition. \n")

# line breaks so commands will not looked jumbled and are easy to read.
num1 = int(input("Choose your first number. \n"))
num2 = int(input("Choose your second number. \n"))
newNumber = num1 + num2

# Output shows users what data to expect.
print(num1, '+', num2, '=', newNumber)