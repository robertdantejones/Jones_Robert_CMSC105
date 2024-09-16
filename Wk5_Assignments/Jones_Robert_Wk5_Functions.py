'''
Name: Robert Jones
Date: 9/15/2024
Purpose: The purpose of this program is to provide an use example of functions in python.
Version: 1.0
'''

# provide a user defined function for user input to be formulated with addition
def calculate_addition(addend1, addend2):
    return addend1 + addend2

# main function for user to interact with
def main():
    print("Choose two numbers to add together \n")
    # provide user input as arguments for user defined function
    addend1 = int(input("Choose first number: \n"))
    addend2 = int(input("Choose second number: \n"))
    # call to user defined function
    total = calculate_addition(addend1, addend2)
    # display output
    print(f'{addend2} + {addend2} = {total}')

# call to main function
if __name__ == "__main__":
    main()



