import unittest
from source.p3 import findsubstring

class checkTheSubstring(unittest.TestCase):
    def test_substring1(self):
        self.assertIs(findsubstring('alphabets', 'lph'), True, 'Failure')
    def test_substring2(self):
        self.assertIs(findsubstring('checking', 'chck'), False, 'Failure')
    def test_substring3(self):
        self.assertIs(findsubstring('12345', '34'), True, 'Failure')
    def test_not_substring4(self):
        self.assertEqual(findsubstring('alpha', 'alphabets'), 'Not valid substring', 'Failure')

if __name__ == "__main__":
    unittest.main()