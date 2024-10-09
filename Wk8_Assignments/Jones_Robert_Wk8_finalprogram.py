'''
Name:
Purpose: The purpose of this program is to provide the user with a
system to borrow available books and return books to be available.
Version: 1.0
Date: 10/7/24
'''


# function to remove book from avail list and adding to borrow list
def catalog(books):
    avail_books.remove(books)
    borrow_books.append(books)
    print(f'You are borrowing {books}.')
    return books
# function to remove book from borrow list and adding to avail list
def borrower(books):
    borrow_books.remove(books)
    avail_books.append(books)
    print(f'You have returned {books}.')
    return books

# main function for user interactivity
def main():
    # declare lists
    avail_books = ['The Name of the Wind', 'Dune', 'The Girl with the Dragon Tattoo', 'The Nightingale','The Hating Game', 'The Shining', 'Becoming', 'The Hunger Games', 'Maus', 'Atomic Habits']
    borrow_books = []
    print('Welcome to your local library!\n')

    while True:
        # Display menu options
        print('Please choose from the options below:\n')
        print('Menu')
        print('1. Borrow a book.')
        print('2. Return a book.')
        print('3. Display available books and books you are borrowing.')
        print('4. Exit the program.\n')

        # user input
        choice=int(input('Choose your option:\n'))

        # decision based of user inputs
        if choice == 1:
            # displaying avail book list w/o punctuation
            while choice == 1:
                 for book in avail_books:
                    print(book)
                 book_borrow=str(input("\nType the name of the book you would like to borrow:\n"))
                 # user validation
                 if book_borrow not in avail_books:
                     print("Invalid entry. Please enter available title.")
                 else:
                    catalog(book_borrow)
                    break
        elif choice == 2:
            while choice == 2:
                for book in borrow_books:
                    print(book)
                book_return=str(input('Type the name of the book that you would like to return:\n'))
                # user validation
                if book_return not in borrow_books:
                    print('Invalid entry. Please enter correct title.')
                else:
                    borrower(book_return)
                    break
        elif choice == 3:
            # displaying current state of lists
            print('Available books:')
            for book in avail_books:
                print(book)
            # checks if borrowed book list is empty
            if len(borrow_books) == 0:
                print("You haven't borrowed any books yet!")
            else:
                print('\nYou are borrowing:')
                for book in borrow_books:
                    print(book)
        elif choice == 4:
            # quit program
            print('You have one week to return your book(s). Goodbye!')
            break
        else:
            # user validation
            print("Invalid choice. Please select from the options displayed on the menu!")


if __name__ == "__main__":
    main()

