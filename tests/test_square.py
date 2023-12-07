import unittest
from square import area
from square import perimeter

class MyTestCase(unittest.TestCase):
    def test_area(self):
        self.assertEqual(area(5), 25)
    def test_perimeter(self):
        self.assertEqual(perimeter(4), 16)



if __name__ == '__main__':
    unittest.main()
