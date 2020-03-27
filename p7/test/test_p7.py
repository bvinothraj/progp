import unittest
from source.p7 import createMyList

class checkMyList(unittest.TestCase):
    def test_checkList(self):
        self.assertEqual(createMyList([1,2,5,5,2,6,4,1]), [1,2,5,6,4], 'Failure')

if __name__ == '__main__':
    unittest.main()