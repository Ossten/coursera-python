import a1
import unittest


class TestSwapK(unittest.TestCase):
    """ Test class for function a1.swap_k. """

    def test_normal_integer(self):
        """Tests for normal integer values of the array"""

        nums = [1, 2, 3, 4, 5, 6]
        actual = a1.swap_k(nums, 2)
        expected = [5, 6, 3, 4, 1, 2]
        self.assertEqual(actual,expected)
    
    def test_normal_string(self):
        """Tests for k greater than the half of the array"""

        nums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        actual = a1.swap_k(nums, 7)
        expected = -1
        self.assertEqual(actual,expected)
    
    def test_empty_list(self):
        """Tests for empty list"""

        nums = []
        actual = a1.swap_k(nums, 3)
        expected = -1
        self.assertEqual(actual,expected)
    
    def test_normal_string(self):
        """Tests for string values of the array"""

        nums = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'j']
        actual = a1.swap_k(nums, 3)
        expected = ['g', 'h', 'j', 'd', 'e', 'f', 'a', 'b', 'c']
        self.assertEqual(actual,expected)
    
    

if __name__ == '__main__':
    unittest.main(exit=False)