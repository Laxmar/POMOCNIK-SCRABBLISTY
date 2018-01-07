

import regex


class IncorrectInputException(Exception):
    pass

# returns list with 2 elements:
# 0: limits of board ex: *M..A*
# 1: available letters: ex: ZRKLIW_
def parse_user_input(user_input):
    user_input = str(user_input).upper().strip()
    pattern = "[.*+]?([A-Ż][.*+]*[A-Ż]*)+[.*+]? [A-Ż_]{1,7}"
    result = regex.fullmatch(pattern, user_input, regex.UNICODE)

    if result is None: raise IncorrectInputException(user_input)

    elements = str(user_input).split(" ")
    return elements


def read_words_from_dictionary():
    words = []
    with open("../slowa.txt", "r+") as file:
        for line in file:
            words.append(line.upper().strip("\n"))

    print("Read file with " + str(len(words)) + " words")
    return words
