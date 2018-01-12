import unittest

from src.input import parse_user_input, IncorrectInputException


class ParseUserInputTestCase(unittest.TestCase):

    correctInput = "*M..A* ZRKLWI"

    def test_result_is_two_elements_list(self):
        parsed_input = parse_user_input(self.correctInput)
        self.assertIsInstance(parsed_input, list)
        self.assertEqual(len(parsed_input), 2)

    def test_raises_exception_when_invalid_input(self):

        incorrect_inputs = ["", "nospace", "num 532", "32 s", "a b c", "ABC ", "**A+A ZZ", "!!A+A xx?da", "*M..A* ABCDEFGHJKLM"]

        for incorrect_input in incorrect_inputs:
            with self.assertRaises(IncorrectInputException) as cm:
                parse_user_input(incorrect_input)

            the_exception = cm.exception
            self.assertIsInstance(the_exception, IncorrectInputException)

    def test_correct_parsed(self):
        correct_inputs_outputs = {
            "*M..A* ZRKLWI": ["*M..A*", "ZRKLWI"],
            "*M..AA* Z": ["*M..AA*", "Z"],
            "*M..A.A* Z": ["*M..A.A*", "Z"],
            "M..A Z": ["M..A", "Z"],

            "MA. Z": ["MA.", "Z"],
            "  MA. Z  ": ["MA.", "Z"],
            "MA. Z_A  ": ["MA.", "Z_A"],
            "MA. Ę_Ą": ["MA.", "Ę_Ą"],
        }
        for correct_input,output in correct_inputs_outputs.items():
            self.assertListEqual(parse_user_input(correct_input), output)


if __name__ == '__main__':
    unittest.main()
