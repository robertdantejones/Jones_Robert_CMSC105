'''
Name:
Purpose: The purpose of this program is to provide the user with a
system to borrow available books and return books to be available.
Version: 1.0
Date: 10/7/24
'''

# declare lists
avail_books=[]
borrow_books=[]

# main function for user interactivity
def main():
    print('Welcome to your local library!\n')

    while True:
        # Display menu options
        print('Please choose from the options below:\n')
        print('Menu')
        print('1. Borrow a book.')
        print('2. Return a book.')
        print('3. Display available books and books you have borrowed.')
        print('4. Exit the program.\n')

        # user input
        choice=int(input('Choose your option:\n'))

        # decision based of user inputs
        if choice == 1:
            # removing book from avail list and adding to borrow list
            print(avail_books)
            book_borrow=input("Type the name of the book you would like to borrow:\n")
            avail_books.remove(book_borrow)
            borrow_books.append(book_borrow)
            print(f'You are borrowing {book_borrow}.')
        elif choice == 2:
            # removing book from borrow list and adding to avail list
            print(borrow_books)
            book_return=input('Type the name of the book that you would like to return:\n')
            borrow_books.remove(book_return)
            avail_books.append(book_return)
            print(f'You have returned {book_return}.')
        elif choice == 3:
            # displaying current state of lists
            print(avail_books)
            # checks if borrowed book list is empty
            if len(borrow_books) == 0:
                print("You haven't borrowed any books yet!")
            else:
                print(borrow_books)
        elif choice == 4:
            # quit program
            print('You have exited the program. Goodbye!')
            break
        else:
            # user validation
            print("Invalid choice. Please select from the options displayed on the menu!")




