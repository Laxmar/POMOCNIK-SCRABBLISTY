import unittest

from src.parseInput import read_words_from_dictionary


class ReadFileTestCase(unittest.TestCase):
    def test_is_return_list(self):
        result = read_words_from_dictionary()
        self.assertIsInstance(result, list)
        self.assertNotEqual (len(result), 0)


if __name__ == '__main__':
    unittest.main()
