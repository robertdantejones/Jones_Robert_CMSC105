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
    print('Welcome to your Movie Recommendations!\n')
    while True:
        # Display menu options
        print('Menu')
        print('1. Add movie to your list.')
        print('2. Remove movie from your list.')
        print("3. View Programmer's recommendations.")
        print('4. Display your list.')
        print('5. Exit the program.\n')

        # gather user input
        choice=int(input("Select from the following options:\n"))
        # decisions based of user input
        if choice == 1:
            # adding movie to list
            add_movie=input("Type the name of movie you want to add:\n")
            movie.append(add_movie)
            print(f'{add_movie} has been added to your list\n')
        elif choice == 2:
            # removing movie from list
            print(movie)
            remove_movie=input('What movie would you like to remove?:\n')
            movie.remove(remove_movie)
            print(f'{remove_movie} has been removed from your list.')
        elif choice == 3:
            # display my recommendations
            my_recommendations=['Lucy','John Wick','Deadpool and Wolverine','Avengers: Endgame','Rebel Ridge','Hustler','Harley Quinn']
            print(my_recommendations)
        elif choice == 4:
            # checks if list is empty
            if len(movie) == 0:
                print("Your list is empty. Please add movies.")
            else:
                # display user's movie list
                 print(movie)
                 print('\n')

        elif choice == 5:
            # quit program
            print('You have exited the program.')
            break
        else:
            # user validation
            print('Invalid Choice. Please choose from the following menu.\n')


if __name__ == "__main__":
    main()