import unittest
import duplicates

class TestRemoveShared(unittest.TestCase):
    """Tests for function duplicates.remove_shared."""
    def test_general_case(self):
        """
        Test remove_shared where there are items that appear in 
        both lists, and intems that appear in only one or othe other list.
        """

        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = [2, 4, 5, 7]

        list_1_expected = [1, 3, 6]
        list_2_expected = [2, 4, 5, 7]

        duplicates.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)

    def test_if_array(self):
        """
        Test remove_shared if the output is of type list.
        """
        list_1 = [1, 2, 3, 4, 5, 6]
        list_2 = [2, 4, 5, 7]

        duplicates.remove_shared(list_1,list_2)

        self.assertEqual(isinstance(list_1, list), True)
        self.assertEqual(isinstance(list_2, list), True)

    def test_long_array(self):
        """
        Test remove_shared where there are items that appear in 
        both lists, and intems that appear in only one or othe other list.
        """
        list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        list_2 = [2, 4, 5, 7]

        list_1_expected = [1, 3, 6, 8, 9, 10]
        list_2_expected = [2, 4, 5, 7]

        duplicates.remove_shared(list_1, list_2)

        self.assertEqual(list_1, list_1_expected)
        self.assertEqual(list_2, list_2_expected)






if __name__ == '__main__':
    unittest.main(exit=False)
    # remove_shared(list_1, list_2)
    # >>> list_1
    # [1, 3, 6]
    # >>> list_2
    # [2, 4, 5, 7]