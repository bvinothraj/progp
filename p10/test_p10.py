import unittest
from p10 import reverse_myList

class check_reversed_list(unittest.TestCase):
    def test_chk_rev1(self):
        self.assertEqual(reverse_myList([2,2,5,3,7,2,88,7,1]), [1,7,88,2,7,3,5,2,2], 'Failure')
    def test_chk_rev2(self):
        self.assertEqual(reverse_myList([1,2,3,4,5]), [5,4,3,2,1], 'Failure')
    def test_chk_rev3(self):
        self.assertEqual(reverse_myList([2,1]), [1,2], 'Failure')

if __name__ == '__main__':
    unittest.main()