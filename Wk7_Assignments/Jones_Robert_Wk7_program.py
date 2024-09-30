'''
Name: Robert Jones
Purpose: The purpose of this program is to create an interactive movie recommendations list.
Version: 1.0
Date: 9/30/24
'''

# main function for interactivity
def main():
    # declare list
    movie = []
    while True:
        # Display menu options
        print('Welcome to your Movie Recommendations!')
        print('1. Add movie to list\n')
        print('2. Remove movie from list\n')
        print("3. View Programmer's recommendations \n")
        print('4. Display list.\n')
        print('5. Exit the program\n')

        # gather user input
        choice=int(input("Select from the following options:\n"))
        # decisions based of user input
        if choice == 1:
            # adding movie to list
            add_movie=input("Type the name of movie your adding to your list:\n")
            movie.append(add_movie)
            print(f'{add_movie} has been added to your list\n')



if __name__ == "__main__":
    main()