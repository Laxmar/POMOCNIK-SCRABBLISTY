import unittest

from src.input import read_words_from_dictionary
from src.solver import find_words


class FindWordsTestCase(unittest.TestCase):

    def setUp(self):
        self.dictionary_words = read_words_from_dictionary()

    def test_find_aa(self):
        found_words = find_words("A. ABC", self.dictionary_words)
        self.assertEqual(found_words, ["AA"])

    def test_find_aa_ad(self):
        found_words = find_words("A. ABCD", self.dictionary_words)
        self.assertEqual(found_words, ["AA", "AD"])

    def test_find_rybak_bak_byk(self):
        found_words = find_words("*B.K* RYA", self.dictionary_words)
        self.assertListEqual(found_words, sorted(["RYBAK", "BAK", "BYK", "BYKA"]))

    def test_blank(self):
        found_words = find_words("B.K _", self.dictionary_words)
        self.assertListEqual(found_words, sorted(['BAK', 'BEK', 'BOK', 'BUK', 'BYK']))

    def test_polish_letters(self):
        found_words = find_words("A. ABCŻ", self.dictionary_words)
        self.assertEqual(found_words, ["AA", "AŻ"])

    def test_double_start(self):
        found_words = find_words("*ŻA* LDEF_R" , self.dictionary_words)
        self.assertEqual(found_words, ['DOŻA', 'DRAŻA', 'DRŻAŁ', 'DUŻA', 'DŻAG', 'DŻAUL', 'DŻAULE', 'DŻAZ', 'GREŻA', 'JEŻA', 'LEŻA', 'LEŻAK', 'LEŻAŁ', 'LOŻA', 'RADŻA', 'RÓŻA', 'RYŻA', 'RŻAŁ', 'RŻANE', 'SERŻA', 'UŻAL', 'ZDŻAR', 'ŻAB', 'ŻAD', 'ŻADEM', 'ŻADEN', 'ŻADNE', 'ŻADU', 'ŻADY', 'ŻAGLE', 'ŻAK', 'ŻAL', 'ŻALĄ', 'ŻALE', 'ŻALEM', 'ŻALEŃ', 'ŻALĘ', 'ŻALI', 'ŻALNE', 'ŻALU', 'ŻALŻE', 'ŻANR', 'ŻAR', 'ŻARĆ', 'ŻAREŁ', 'ŻAREM', 'ŻAREN', 'ŻARLE', 'ŻARLI', 'ŻARŁ', 'ŻARN', 'ŻARNE', 'ŻART', 'ŻARTE', 'ŻARU', 'ŻARY', 'ŻARZ', 'ŻARZE'])

if __name__ == '__main__':
    unittest.main()
