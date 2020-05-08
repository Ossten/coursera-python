import a1
import unittest


class TestStockPriceSummary(unittest.TestCase):
    """ Test class for function a1.stock_price_summary. """
    
    def test_general_case(self):
        """Tests for normal integer values of the array"""
        actual = a1.stock_price_summary([1, 2, 3, 4, 5, 6, -20, -5])
        expected = (21, -25)
        self.assertEqual(actual,expected)

    def test_all_zeros(self):
        """Tests for all zeros values of the array"""
        actual = a1.stock_price_summary([0, 0, 0, 0, 0, 0, 0, 0])
        expected = (0, 0)
        self.assertEqual(actual,expected)
    
    def test_empty_array(self):
        """Tests for empty array"""
        actual = a1.stock_price_summary([])
        expected = (0,0)
        self.assertEqual(actual,expected)
        
    


if __name__ == '__main__':
    unittest.main(exit=False)