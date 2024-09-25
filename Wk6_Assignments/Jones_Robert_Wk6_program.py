'''
Name: Robert Jones
Date:9/24/24
Purpose:The purpose of this program is to display a mad libs story involving random words from user input.
Version:1.0
'''

# format user input
def text_format(*text):
    for spaces in text:
        format= spaces.strip()
        return format

# main function for user input
def main():
    # introduce program
    print("Welcome to Mad Libs!\n")
    print("A story will be create with the help of you.\n")
    print("You will be prompted to enter your name, two verbs, two nouns, two adjectives, and two integers.\n")

    # get user input
    name=input("What is your name?\n")
    verb1=input("Enter a verb ending in -ing:\n")
    verb2=input("Enter a verb:\n")
    plural_noun=input("Enter a plural noun:\n")
    noun=input("Enter a noun:\n")
    adjective1=input("Enter your first adjective:\n")
    adjective2=input("Enter your second adjective;\n")
    integer1=int(input("Choose a number:\n"))
    integer2=int(input("Choose another number:\n"))
    animal=input("Choose an animal:\n")
    food=input("Pick a food:\n")
    emotion=input("Pick an emotion:\n")
    liquid=input("Pick a liquid:\n")

    #call user defined function
    format_name=text_format(name)
    format_verb1=text_format(verb1)
    format_verb2=text_format(verb2)
    format_plural=text_format(plural_noun)
    format_noun=text_format(noun)
    format_adjective1=text_format(adjective1)
    format_adjective2=text_format(adjective2)
    format_animal=text_format(animal)
    format_food=text_format(food)
    format_emotion=text_format(emotion)
    format_liquid=text_format(liquid)

    # print mad lib story
    print('Mad Libs: A Day at the Beach\n')
    print(f'It was a/an {format_adjective1}nday, and {format_name} decided to go to the beach with their {format_noun}. They packed their {format_plural} and set off. When they arrived, the sun was {format_verb1}, and the ocean looked so {format_adjective2}.\n')
    print(f'First, they set up their {format_noun} on the sand. {format_name} applied {format_noun} to protect their skin from the {format_adjective2} sun. Then, they ran into the water and started {format_verb1}. Suddenly, a {format_adjective1} {format_animal} swam by, which made {format_name} {format_verb2} in surprise!\n')
    print(f'After {integer1} minutes of swimming, they decided to build a/an {format_adjective1} sandcastle with {format_plural}. It was {integer2} feet tall and the most {format_adjective1} castle {format_name} had ever seen! Later, they ate some {format_food} and drank {format_liquid} while watching the sunset.\n')
    print(f'As the day ended, {format_name} thought about how {format_adjective2} it was to spend time with their {format_noun} at the beach. They left feeling {format_emotion} and ready for another {format_adjective2} adventure tomorrow!\n')

# call to main function
if __name__ == "__main__":
    main()
