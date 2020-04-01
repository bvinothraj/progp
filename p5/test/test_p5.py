import unittest
from source.p5 import findindex

class checkTheIndex(unittest.TestCase):

    def test_theIndex1(self):
        self.assertEqual(findindex('elephant', 'e'), 0, 'Failure')
    def test_theIndex2(self):
        self.assertEqual(findindex('elephant', 'z'), -1, 'Failure')
    def test_theIndex3(self):
        self.assertEqual(findindex('elephant', 'ze'), -1, 'Failure')

if __name__ == "__main__":
    unittest.main()