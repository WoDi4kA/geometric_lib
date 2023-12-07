import unittest
from rectangle import area
from rectangle import perimeter


class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(3, 3), 9)
    def test_perimeter(self):
        self.assertEqual(perimeter(4, 7), 22)



if __name__ == '__main__':
    unittest.main()
