import locale
import unittest

from src.input import read_words_from_dictionary, create_letter_score_dict


class ReadFileTestCase(unittest.TestCase):
    def test_is_return_list(self):
        result = read_words_from_dictionary()
        self.assertIsInstance(result, list)
        self.assertNotEqual (len(result), 0)
        self.assertEqual(result[0], "AA")

    def test_polish_letters(self):
        result = read_words_from_dictionary()
        self.assertIsInstance(result, list)
        self.assertNotEqual (len(result), 0)
        self.assertTrue(result.__contains__("AŻ"))


class CreateLetterScoreMap(unittest.TestCase):
    def test_is_dict(self):
        res = create_letter_score_dict()
        print(res)
        self.assertIsInstance(res, dict)

    def test_is_contain_all_letters(self):
        res = create_letter_score_dict()
        self.assertIsInstance(res, dict)
        letters = "WEĘRTYUIOÓPAĄŚSDFGHJKLŁŻZŹCĆBŃNM"
        self.assertEqual(len(letters), len(res))
        for let in list(letters):
            if not res.__contains__(let):
                self.fail(let)


if __name__ == '__main__':
    unittest.main()
