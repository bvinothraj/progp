import unittest
from source.p3 import findsubstring

class checkTheSubstring(unittest.TestCase):
    def test_substring(self):
        a = 'alphabets'
        b = 'lph'
        output = findsubstring(a, b)
        actualResult = True
        self.assertIs(output, actualResult, 'Failure')

    def test_not_substring(self):
        a = 'alpha'
        b = 'alphabets'
        output = findsubstring(a, b)
        actualResult = 'Not valid substring'
        self.assertEqual(output, actualResult, 'Failure')

if __name__ == "__main__":
    unittest.main()
