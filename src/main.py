#
#   1. Parse user input
#   2. Load dictionary with polish words
#   3. Find matching words
#   4. Calculate points for words
#   5. Return sorted by points list of words
#
import operator

from src.input import parse_user_input, IncorrectInputException, read_words_from_dictionary, create_letter_score_dict
from src.solver import find_words

if __name__ == '__main__':
    print("Starting program")

    words = read_words_from_dictionary()
    letter_score_dict = create_letter_score_dict()

    while True:
        user_input = input("Enter phrase or 'q' to exit program  ")
        if user_input is "q": break

        try:
            found_words = find_words(user_input, words)
            map_letter_to_score = lambda letter: letter_score_dict.get(letter)
            words_with_score = {word: sum(map(map_letter_to_score, word)) for word in found_words}
            sorted_words = sorted(words_with_score.items(), key=operator.itemgetter(1), reverse=True)

            if len(sorted_words) == 0:
                print("Sorry any words match")
                continue

            for w,s in sorted_words:
                print(str(w)+ " \t " + str(s))

        except IncorrectInputException:
            print("Incorrect input please try again")
