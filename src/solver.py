import regex


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
    #letters_number_on_board = list(filter(lambda ch: str(ch).isalpha(), regex.sub("\[.*]", "", pattern))).__len__()
    word_max_length = player_letters_number + letters_number_on_board
    filtered_words = list(filter(lambda word: len(word) <= word_max_length, words))
    return filtered_words


def match_words(words, player_letters, letters_on_board):
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


