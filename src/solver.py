import regex

from src.input import parse_user_input


def create_pattern(parsed_input):
    limits = str(parsed_input[0])
    available_characters = parsed_input[1]

    pattern_list = "[" + str(available_characters) + "]"

    if "_" in available_characters:
        pattern_list = "[A-Ż]"

    pattern = limits.replace(".", pattern_list)
    pattern = pattern.replace("+", pattern_list + "+")
    pattern = pattern.replace("*", pattern_list + "*")

    return pattern


def filter_using_regex(words, pattern):
    filtered_words = list(filter(lambda word: regex.fullmatch(pattern, word, regex.UNICODE) is not None, words))
    return filtered_words


def filter_word_max_length(words, letters_number_on_board, player_letters_number):
    word_max_length = player_letters_number + letters_number_on_board
    filtered_words = list(filter(lambda word: len(word) <= word_max_length, words))
    return filtered_words


def match_words(words: list, player_letters: list, letters_on_board: list):
    available_letters = player_letters + letters_on_board
    blanks_number = len(list(filter(lambda letter: letter == "_", player_letters)))
    matched_words = []
    for word in words:
        word_copy = word
        for letter in available_letters:
            word_copy = word_copy.replace(letter, "", 1)
        if word_copy == "" or blanks_number == len(word_copy) :
            matched_words.append(word)
    return matched_words


def find_words(user_input: str, dictionary_words: list):
    print("Finding words... ")
    parsed_input = parse_user_input(user_input)
    pattern = create_pattern(parsed_input)

    letters_on_board = list(filter(lambda letter: str(letter).isalpha(), str(user_input).split(" ")[0]))
    players_letters = list(filter(lambda letter: str(letter).isalpha() or letter == "_", str(user_input).split(" ")[1]))

    filtered_words = filter_using_regex(dictionary_words, pattern)
    filtered_words = filter_word_max_length(filtered_words, len(letters_on_board), len(players_letters))
    matched_words = match_words(filtered_words, players_letters, letters_on_board)

    return matched_words
