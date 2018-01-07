
#
#   1. Parse user input
#   2. Load dictionary with polish words
#   3. Find matching words
#   4. Calculate points for words
#   5. Return sorted by points list of words
#

from src.parseInput import parse_user_input, IncorrectInputException, read_words_from_dictionary

if __name__ == '__main__':
    print("Starting program")

    words = read_words_from_dictionary()

    while True:
        user_input = input("Enter phrase or 'q' to exit program  ")
        if user_input is "q": break

        try:
            res = parse_user_input(user_input)
            print(res)
        except IncorrectInputException:
            print("Incorrect input please try again")
