import unittest
from exercises import *

class Test(unittest.TestCase):

    """
    Verifies the functionality of the JTR rule parser
    """

    def test_create_random(self):

        self.assertEqual(len(create_random(4,212)),4)

    def test_double_list(self):
        self.assertEqual(double_list([]), [])
        self.assertEqual(double_list([1]), [2])
        self.assertEqual(double_list([1,2,3]), [1,4,6])

    def test_abbreviate(self):

        l = ['dog', 'cat', 'shoe']
        d = {'d': 'dog', 'c': 'cat', 's': 'shoe'}

        self.assertEqual(abbreviate(l),d)

    def list_of_lists(self):

        x = [['X', 'X', 'X'], ['X', 'X', 'X'],['X', 'X', 'X']]

        self.assertEqual(list_of_lists(3), x)
        
if __name__ == "__main__":

    rule_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    rule_runner = unittest.TextTestRunner()
    rule_runner.run(rule_suite)