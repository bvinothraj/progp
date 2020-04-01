import unittest
from source.p7 import createMyList

class checkMyList(unittest.TestCase):
    def test_checkList1(self):
        self.assertEqual(createMyList([1,2,5,5,2,6,4,1]), [1,2,5,6,4], 'Failure')
    def test_checkList2(self):
        self.assertEqual(createMyList([1,1,1,1,1,2]), [1,2], 'Failure')    
    def test_checkList3(self):
        self.assertEqual(createMyList([7]), [7], 'Failure')

if __name__ == '__main__':
    unittest.main()