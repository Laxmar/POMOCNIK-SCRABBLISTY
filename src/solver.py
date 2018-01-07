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
    # TODO add filter using characters number
    return filtered_words
