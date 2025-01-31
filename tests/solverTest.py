import unittest

from src.input import read_words_from_dictionary
from src.solver import create_pattern, filter_using_regex, filter_word_max_length, match_words


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

    def test_polish_letters2(self):
        filtered_words = filter_using_regex(["AA","AŻ", "AD", "AZ"], "A[ABCDŻ]")
        self.assertEqual(["AA", "AŻ", "AD"], filtered_words)

    def test_three_words(self):
        filtered_words = filter_using_regex(["BAK", "BAR", "RYBAK"], "B[ARKŻ]+")
        self.assertEqual(["BAK", "BAR"], filtered_words)

    def test_complex(self):
        filtered_words = filter_using_regex(["BAK", "BAR", "RYBAK"], "[ABRKYŻ]*B[ABRKYŻ][ABKRKŻ]*")
        self.assertEqual(["BAK", "BAR", "RYBAK"], filtered_words)

    # def test_using_words_from_file(self):
    #     words = read_words_from_dictionary()
    #     filtered_words = filter_using_regex(words, "[ABRKYŻ]*B[ABRKYŻ][ABKRKŻ]*")
    #     self.assertIsInstance(filtered_words, list)
    #     self.assertTrue("BAK" in filtered_words)
    #     self.assertTrue("BAR" in filtered_words)
    #     self.assertTrue("RYBAK" in filtered_words)


class FilterUsingWordMaxLengthTestCase(unittest.TestCase):
    def test_simples(self):
        filtered_words = filter_word_max_length(["AA"], 1, 2)
        self.assertIsInstance(filtered_words, list)
        self.assertEqual(filtered_words, ["AA"])

    def test_all_words_shorter(self):
        words = ["BAK", "BAR", "RYBAK", "ŻABA" ]
        filtered_words = filter_word_max_length(words, 3, 7)
        self.assertEqual(filtered_words, words)

    def test_length_equal(self):
        words = ["BAK", "BAR"]
        filtered_words = filter_word_max_length(words, 1, 2)
        self.assertEqual(filtered_words, words)

    def test_length_lower(self):
        words = ["AA", "BAK", "BAR"]
        filtered_words = filter_word_max_length(words, 1, 1)
        self.assertEqual(filtered_words, ["AA"])


class MatchWordsTestCase(unittest.TestCase):
    def test_simplest_match(self):
        matched_words = match_words(["AA"], ["A", "B"], ["A"])
        self.assertIsInstance(matched_words, list)
        self.assertEqual(["AA"], matched_words)

    def test_simplest_double_match(self):
        words = ["AB", "AA"]
        matched_words = match_words(words, ["A", "B"], ["A"])
        self.assertEqual(words, matched_words)

    def test_no_match(self):
        words = ["AB", "AA"]
        matched_words = match_words(words, ["K", "J"], ["A"])
        self.assertEqual([], matched_words)

    def test_more_letters(self):
        words = ["BAK", "BAR", "RYBAK", "ŻABA"]
        matched_words = match_words(words, ["R", "K", "Y", "Ż", "A"], ["A", "B"])
        self.assertEqual(words, matched_words)

    def test_one_blank(self):
        words = ["BAK", "BAR"]
        matched_words = match_words(words, ["O", "_"], ["A", "B"])
        self.assertEqual(words, matched_words)

    def test_two_blanks(self):
        words = ["BAK", "BAR"]
        matched_words = match_words(words, ["O", "_", "_"], ["B"])
        self.assertEqual(words, matched_words)

    def test_complex(self):
        words = ["BAK", "BAR", "RYBAK", "ŻABA", "JAREK"]
        matched_words = match_words(words, ["R", "K", "Y","_", "A"], ["A", "B"])
        self.assertEqual(["BAK", "BAR", "RYBAK", "ŻABA"], matched_words)

    def test_polish_letters(self):
        matched_words = match_words(["AA", "AŻ", "AD"], ["A", "B", "D", "Ż"], ["A"])
        self.assertIsInstance(matched_words, list)
        self.assertEqual(["AA", "AŻ", "AD"], matched_words)


if __name__ == '__main__':
    unittest.main()
