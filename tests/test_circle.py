import unittest
import math
from circle import area
from circle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 78.53981633974483)
    def test_perimeter(self):
        self.assertEqual(perimeter(4), 25.132741228718345)



if __name__ == '__main__':
    unittest.main()
