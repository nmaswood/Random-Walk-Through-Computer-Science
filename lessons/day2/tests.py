import unittest
from exercises import *

#sys_path.append(os_path.abspath('../src'))

class Test(unittest.TestCase):

    """
    Verifies the functionality of the JTR rule parser
    """

    def test_f_to_c(self):

        self.assertEqual(f_to_c(212),100)
        self.assertEqual(f_to_c(-32),0)
        self.assertEqual(f_to_c(-40),-40)

    def test_sum_to_n_even(self):

        self.assertEqual(sum_to_n_even(7),12)
        self.assertEqual(sum_to_n_even(8),20)
        self.assertEqual(sum_to_n_even(9),20)

    def test_count_three(self):

        return 14

    def test_puncutate(self):

        self.assertEqual(punctuate('eggs tuna cheese milk potatoes vinegar oil'), 'eggs,tuna,cheese,milk,potatoes,vinegar,oil' )

    def test_exagerate(self):


        self.assertEqual(exagerate(4, 'smart'), 'I am really really really really smart')




if __name__ == "__main__":

    rule_suite = unittest.TestLoader().loadTestsFromTestCase(Test)
    rule_runner = unittest.TextTestRunner()
    rule_runner.run(rule_suite)