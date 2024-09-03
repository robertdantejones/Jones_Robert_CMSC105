'''
Name: Robert Jones
Date: 8/27/2024
Purpose: The purpose of this program is to provide calculations for the user using addition, subtraction, multiplication, and divison.
Version: 1.0
'''

# Create prompt to state what program is for.
print("Welcome to Calculator. You are able to add, subtract, multiply, and divide")

# Gather user input
num1 = int(input("Choose your first number. \n"))
num2 = int(input("Choose your second number. \n"))
num3 = int(input("Choose your third number. \n"))
num4 = int(input("Choose your fourth number. \n"))

# Processing: Addition calculations
addNum1 = num1 + num2
addNum2 = num3 + num4
addNum3 = num1 + num3
addNum4 = num2 + num4

# Processing: Subtraction calculations
subNum1 = num1 - num2
subNum2 = num3 - num4
subNum3 = num1 - num3
subNum4 = num2 - num4

# Processing: Multiplication calculations
mulNum1 = num1 * num2
mulNum2 = num3 * num4
mulNum3 = num1 * num3
mulNum4 = num2 * num4

# Processing: Division calculations
divNum1 = num1 / num2
divNum2 = num3 / num4
divNum3 = num1 / num3
divNum4 = num2 / num4

# Output: Display results
print("Total using addition:", num1, '+', num2, '=', addNum1)
print("Total using addition:", num3, '+', num4, '=', addNum2)
print("Total using addition:", num1, '+', num3, '=', addNum3)
print("Total using addition:", num2, '+', num4, '=', addNum4, '\n')

print("Total using subtraction:", num1, '-', num2, '=', subNum1)
print("Total using subtraction:", num3, '-', num4, '=', subNum2)
print("Total using subtraction:", num1, '-', num3, '=', subNum3)
print("Total using subtraction:", num2, '-', num4, '=', subNum4, '\n')

print("Total using multiplication:", num1, '*', num2, '=', mulNum1)
print("Total using multiplication:", num3, '*', num4, '=', mulNum2)
print("Total using multiplication:", num1, '*', num3, '=', mulNum3)
print("Total using multiplication:", num2, '*', num4, '=', mulNum4, '\n')

print("Total using division:", num1, '/', num2, '=', divNum1)
print("Total using division:", num3, '/', num4, '=', divNum2)
print("Total using division:", num1, '/', num3, '=', divNum3)
print("Total using division:", num2, '/', num4, '=', divNum4, '\n')











