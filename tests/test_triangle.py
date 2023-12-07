import unittest
from triangle import area
from triangle import perimeter

class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(2, 5), 5)
    def test_perimeter(self):
        self.assertEqual(perimeter(4, 6, 9), 19)



if __name__ == '__main__':
    unittest.main()
