import unittest
from source.p2 import checkVowels

class checkTheVowels(unittest.TestCase):
    def test_vowel1(self):
        self.assertDictEqual(checkVowels('alphabets'), {'a': 2, 'e': 1, 'i':0, 'o':0, 'u':0})
    def test_vowel2(self):
        self.assertDictEqual(checkVowels('aeiou'), {'a': 1, 'e': 1, 'i':1, 'o':1, 'u':1})
    def test_vowel3(self):
        self.assertDictEqual(checkVowels('a12523e'), {'a': 1, 'e': 1, 'i':0, 'o':0, 'u':0})
    def test_vowel4(self):
        self.assertDictEqual(checkVowels('AEiou'), {'a': 0, 'e': 0, 'i':1, 'o':1, 'u':1})        

if __name__ == "__main__":
    unittest.main()