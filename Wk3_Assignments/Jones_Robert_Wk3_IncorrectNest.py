'''
Name: Robert Jones
Date: 9/1/2024
Purpose: The purpose of this program is to show a improper way to use nested IF statements
Version: 1.0
'''

# Declare variables
course_1 = "program"
course_2 = "pace"

# nested if statement
if course_1 == "pace":
# The code for the outer statement needs to be indented to avoid IndentationError and execute correct code based on the correct logic
print("It's time to take" + course_1)
    if course_2 != "program":
        print("Its time to take" + course_2)


