import a1
import unittest


class TestNumBuses(unittest.TestCase):
    """ Test class for function a1.num_buses."""
    def test_general_case(self):
        """Tests for normal integer value (470)"""
        actual = a1.num_buses(470)
        expected = 10
        self.assertEqual(actual,expected)
    
    def test_zero(self):
        """ Tests for input of zero (470) """
        actual = a1.num_buses(0)
        expected = 0
        self.assertEqual(actual,expected)
    
    def test_negative(self):
        """ Tests for input of negative integer number """
        actual = a1.num_buses(-10)
        expected = -1
        self.assertEqual(actual,expected)
    
    def test_boundry(self):
        """ Tests for value divisible by 50 """
        actual = a1.num_buses(200)
        expected = 4
        self.assertEqual(actual,expected)
    
    def test_decimal(self):
        """ Tests for decimal number """
        actual = a1.num_buses(65.7)
        expected = 2
        self.assertEqual(actual,expected)

if __name__ == '__main__':
    unittest.main(exit=False)