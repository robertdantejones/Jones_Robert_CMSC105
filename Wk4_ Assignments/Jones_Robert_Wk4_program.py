'''
Name: Robert Jones
Date: 9/11/2024
Purpose: This program is intended to provide calculations for multiples of 7 based on the user's input
Version: 1.0
'''

# Declare variables
start = 1
end = 11
user = int(input('Enter number from 1-11: \n'))

# validate user input
while user >= 1 and user <= 11:
    # print results
    print(f'Multiplication Table for {user}: \n')
    for count in range(start, end +1):
        new = count * user
        print(f"{user} x {count} = {new}")
    # check if user wants to end program
    userQuit = input('Would you like to quit the program (yes/no): \n')
    if userQuit == 'yes':
        break
    # checking validation so while loop can repeat
    elif userQuit == 'no':
        user = int(input('Enter number from 1-11: \n'))
        continue

# when user doesnt enter valid input
while user >= 12 or user < 0:
    # check if user wants to end program
    userQuit = input('Would you like to quit the program (yes/no): \n')
    if userQuit == 'yes':
        break
    elif userQuit == 'no':
        # run multiples based on corrected user input
        userCorrect = int(input('Enter number from 1-11: \n'))
        if userCorrect >= 1 and userCorrect <= 11:
            print(f'Multiplication Table for {userCorrect}: \n')
            for count in range(start, end + 1):
                new = count * userCorrect
                print(f"{userCorrect} x {count} = {new}")













