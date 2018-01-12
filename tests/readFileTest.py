import unittest

from src.input import read_words_from_dictionary


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


if __name__ == '__main__':
    unittest.main()
