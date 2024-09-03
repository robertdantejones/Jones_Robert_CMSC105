'''
Name: Robert Jones
Date: 9/3/2024
Purpose: The purpose of this program is to calculate accurate ticket prices based off age and start time of movie.
Version: 1.0
'''

#Declare variables
age = int(input("How old are you? \n"))
movieTime = int(input("What time does your movie start? \n"))

#child price variables
childPrice = 5
teenPrice = 10
seniorPrice = 7
#movie time price variable
discountTime = 5

#Price for Child Ticket Conditional
if age < 12:
        if movieTime < 5:
            newChildPrice = childPrice-2
            print("Your ticket at a discounted rate is " + str(newChildPrice))
        else:
            print("Your ticket is $" + str(childPrice))

#Price for Teen ticket Conditional
if age >= 12 and age <= 54:
    if movieTime < 5:
        newTeenPrice = teenPrice-2
        print("Your ticket at a discounted rate is $" + str(newTeenPrice))
    else:
        print("Your ticket is $" + str(teenPrice))

#Price for Senior ticket Conditional
if age >= 55:
    if movieTime < 5:
        newSeniorPrice = seniorPrice-2
        print("Your ticket at a discounted rate is $" + str(newSeniorPrice))
    else:
        print("Your ticket is $" + str(seniorPrice))

print("Enjoy your movie!")

