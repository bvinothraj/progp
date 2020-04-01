import unittest
from p9 import findDuplicates

class check_list_duplicates(unittest.TestCase):
    def test_chk_dup1(self):
        self.assertEqual(findDuplicates([2,2,5,3,7,2,88,7,1]), [2,7], 'Failure')
    def test_chk_dup2(self):
        self.assertEqual(findDuplicates([1,2,3,4,5]), [], 'Failure')
    def test_chk_dup3(self):
        self.assertEqual(findDuplicates([2,2,2,2,2]), [2], 'Failure')

if __name__ == '__main__':
    unittest.main()