import unittest
from source.p4 import qsort

class checkQuickSort(unittest.TestCase):
    def test_qsort(self):
        arr1 = [3,7,1,9,23,45,11,5]
        start = 0
        end = len(arr1)
        result = [1,3,5,7,9,11,23,45]
        self.assertEqual(qsort(arr1,start,end), result, 'Failure')

if __name__ == '__main__':
    unittest.main()
