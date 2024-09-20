'''
Name: Robert Jones
Date: 9/18/2024
Purpose: The purpose of this program is create a pizza ordering program
Version: 1.0
'''
# user-defined function for final total
def calculate_finaltotal(size_price, quantity_price):
    return size_price* quantity_price

# input prompts for user to interact with
def main():
    toppings =[]
    print("Welcome to Roberto's Pizzeria! \n")
    print("Choose one size pizza(1 for Small, 2 for Medium, 3 for Large)")
    size_choice=int(input("Enter size choice: \n"))
    # conditionals for pizza size choice
    if size_choice == 1:
        # setting price and size type variable
        pizza = 7
        type = 'Small'
    elif size_choice == 2:
        pizza = 10
        type = 'Medium'
    elif size_choice == 3:
        pizza = 13
        type = 'Large'
    else:
        print("Choice was invalid")


    topping = int(input("Would you like toppings? (1 for yes/2 for no):\n"))
    # conditional for selecting topping
    if topping == 1:
        topping1=int(input("Pepperoni (1 or 0): \n"))
        # conditional for selecting individual topping choice
        if topping1 == 1:
            # adding dollar to pizza base price
            pizza +=1
            # adding topping choice to list to display on reciept
            toppings.append("Pepperoni")
        else:
            pizza+=0

        topping2=int(input("Sausage (1 or 0): \n"))
        if topping2 == 1:
            pizza += 1
            toppings.append("Sausage")
        else:
            pizza += 0
        topping3=int(input("Olive (1 or 0): \n"))
        if topping3 == 1:
            pizza += 1
            toppings.append("Olives")
        else:
            pizza += 0
    elif 1 < topping <= 2:
        pizza += 0
        toppings = 'no toppings selected'

    quantity = int(input("Enter number of pies: \n"))

    # call user-defined final price function
    checkout= calculate_finaltotal(pizza,quantity)

    # Display results for user input
    print("Thank you for your order!")
    print(f'{type} cheese pizza with {toppings} - ${pizza}')
    print(f'Number of quantity: {quantity}')
    print(f'Your final total is ${checkout}')


    # # call total function
    # checkout = calculate_total(size,topping,quantity)

# call to main function
if __name__ == "__main__":
    main()
