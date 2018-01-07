import unittest

from src.parseInput import read_words_from_dictionary
from src.solver import create_pattern, filter_using_regex


class CreatePatternTestCase(unittest.TestCase):
    def test_simplest_pattern(self):
        pattern = create_pattern(["A.", "A"])
        self.assertEqual("A[A]", pattern)

    def test_two_chars(self):
        pattern = create_pattern(["A.", "AB"])
        self.assertEqual("A[AB]", pattern)

    def test_polish_letters(self):
        pattern = create_pattern(["A.", "ĄEC"])
        self.assertEqual("A[ĄEC]", pattern)

    def test_two_dots_between(self):
        pattern = create_pattern(["A..D", "EFG"])
        self.assertEqual("A[EFG][EFG]D", pattern)

    def test_plus(self):
        pattern = create_pattern(["A+", "AB"])
        self.assertEqual("A[AB]+", pattern)

    def test_plus_seven_digit(self):
        pattern = create_pattern(["A+B", "DEFGHJS"])
        self.assertEqual("A[DEFGHJS]+B", pattern)

    def test_star(self):
        pattern = create_pattern(["A*", "AB"])
        self.assertEqual("A[AB]*", pattern)

    def test_dot_star_plus(self):
        pattern = create_pattern(["+A..E*", "DEFGHJS"])
        self.assertEqual("[DEFGHJS]+A[DEFGHJS][DEFGHJS]E[DEFGHJS]*", pattern)

    def test_blank(self):
        pattern = create_pattern(["A..K", "BC_"])
        self.assertEqual("A[A-Ż][A-Ż]K", pattern)



class FilterUsingRegexTestCase(unittest.TestCase):
    def test_simplest(self):
        filtered_words = filter_using_regex(["AA"], "A[A]")
        self.assertIsInstance(filtered_words, list)
        self.assertEqual(["AA"], filtered_words)

    def test_no_match(self):
        filtered_words = filter_using_regex(["AA"], "B[A]")
        self.assertIsInstance(filtered_words, list)
        self.assertEqual([], filtered_words)

    def test_plus(self):
        filtered_words = filter_using_regex(["AA"], "A[A]+")
        self.assertEqual(["AA"], filtered_words)

    def test_star(self):
        filtered_words = filter_using_regex(["AA"], "A[A]*")
        self.assertEqual(["AA"], filtered_words)

    def test_polish_letters(self):
        filtered_words = filter_using_regex(["ĄA"], "Ą[A]*")
        self.assertEqual(["ĄA"], filtered_words)

    def test_three_words(self):
        filtered_words = filter_using_regex(["BAK", "BAR", "RYBAK"], "B[ARKŻ]+")
        self.assertEqual(["BAK", "BAR"], filtered_words)

    def test_complex(self):
        filtered_words = filter_using_regex(["BAK", "BAR", "RYBAK"], "[ABRKYŻ]*B[ABRKYŻ][ABKRKŻ]*")
        self.assertEqual(["BAK", "BAR", "RYBAK"], filtered_words)

    def test_using_words_from_file(self):
        words = read_words_from_dictionary()
        filtered_words = filter_using_regex(words, "[ABRKYŻ]*B[ABRKYŻ][ABKRKŻ]*")
        self.assertIsInstance(filtered_words, list)
        self.assertTrue("BAK" in filtered_words)
        self.assertTrue("BAR" in filtered_words)
        self.assertTrue("RYBAK" in filtered_words)


if __name__ == '__main__':
    unittest.main()
