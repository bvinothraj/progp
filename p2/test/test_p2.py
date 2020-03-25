import unittest
from source.p2 import checkVowels

class checkTheVowels(unittest.TestCase):
    def test_vowel(self):
        a = 'alphabets'
        output = checkVowels(a)
        actualResult = {'a': 2, 'e': 1, 'i':0, 'o':0, 'u':0}
        self.assertDictEqual(output, actualResult)

if __name__ == "__main__":
    unittest.main()
