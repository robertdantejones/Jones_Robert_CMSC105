'''
Name: Robert Jones
Date: 9/8/2024
Purpose: The purpose of this program is to show the proper use of for loops, while loops, and use of control statements.
Version: 1.0
'''

# Assign values to input for loop
start_value=0
end_value=10

# declare for loop to iterate over values set.
for count in range(start_value, end_value):
    if count == 8:
        # continue statement to iterate over 8. not showing in output.
        continue
    print(count)
print("Where is 8?")

# Declare loop control variable for while loop
count = 0

# Declare while loop that iterates until condition is met
while count < 8:
    count +=1
    print(count)
    if count == 7:
        # break statement to exit from while loop so that 8 wont show in output.
        break

print("7 ate 9 and 10")


