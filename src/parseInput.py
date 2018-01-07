

import re


class IncorrectInputException(Exception):
    pass

# returns list with 2 elements:
# 0: limits of board ex: *M..A*
# 1: available letters: ex: ZRKLIW_
def parse_user_input(user_input):
    user_input = str(user_input).upper().strip()
    regex = "[.*+]?([A-Z][.*+]*[A-Z]*)+[.*+]? [A-Z_]{1,7}"
    prog = re.compile(regex)
    result = prog.match(user_input)

    if result is None or len(result.group()) != len(user_input):
        raise IncorrectInputException(user_input)

    elements = str(user_input).split(" ")

    return elements
