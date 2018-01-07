
#
#   1. Parse user input
#   2. Load dictionary with polish words
#   3. Finding matching words: sorted by points
#
#

from src.parseInput import parse_user_input, IncorrectInputException

if __name__ == '__main__':
    print("Starting program")

    while True:
        user_input = input("Enter phrase or 'q' to exit program  ")
        if user_input is "q": break

        try:
            res = parse_user_input(user_input)
            print(res)
        except IncorrectInputException:
            print("Incorrect input please try again")

