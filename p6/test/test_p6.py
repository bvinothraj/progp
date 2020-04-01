import unittest
from source.p6 import reverseString

class checkReversedString(unittest.TestCase):
    def test_checkReverse1(self):
        self.assertEqual(reverseString('alphabets'), 'stebahpla', 'Failed')
    def test_checkReverse2(self):
        self.assertEqual(reverseString('ai'), 'ia', 'Failed')    
    def test_checkReverse3(self):
        self.assertEqual(reverseString('d'), 'd', 'Failed')

if __name__ == '__main__':
    unittest.main()