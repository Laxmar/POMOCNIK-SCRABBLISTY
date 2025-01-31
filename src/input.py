import itertools
import regex
import codecs


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
    with open("../slowa.txt", "r", encoding="utf-8") as file:
        for line in file:
            word = line.upper().strip("\n")
            words.append(word)

    print("Read file with " + str(len(words)) + " words")
    return words


def create_letter_score_dict():
    score_table = [
        (1, "AEINORSWZ"),
        (2, "CDKLMPTY"),
        (3, "BGHJŁU"),
        (5, "ĄĘFÓŚŻ"),
        (6, "Ć"),
        (7, "Ń"),
        (9, "Ź"),
    ]
    letter_score_dict = dict()
    for e in score_table:
        temp = dict(zip( list(e[1]), list(itertools.repeat(e[0], len(e[1])))))
        letter_score_dict.update(temp)
    return letter_score_dict
