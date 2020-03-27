import unittest
from source.p6 import reverseString

class checkReversedString(unittest.TestCase):
    def test_checkReverse(self):
        self.assertEqual(reverseString('alphabets'), 'stebahpla', 'Failed')

if __name__ == '__main__':
    unittest.main()