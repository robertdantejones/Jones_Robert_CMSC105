'''
Name: Robert Jones
Date: 9/23/2024
Purpose: The purpose of this program is show use case of predefined string methods
Version: 1.0
'''


def main():
    # positional type arguments using .format method on string
    food = input("What did you eat today?\n")
    drink = input("What did you drink today? \n")
    digest = "Today I ate {} and drunk {}.\n".format(food,drink)
    print(digest)
    next_meal = int(input("What time are you eating dinner?\n"))

    # average meal time in USA
    if next_meal<6:
        # formatted string literals
        dinner = input("What do you want to eat for dinner?\n")
        drink = input("What do you want to drink with your dinner? \n")
        digest = f'I want to eat {dinner} for dinner with {drink} to drink.'
        print(digest)
    else:
        dessert = input("What did you have for desert? \n")
        sweet_treat = f'Yum! I had {dessert} for dessert.'
        print(sweet_treat)


# call to main function
if __name__ == "__main__":
    main()
