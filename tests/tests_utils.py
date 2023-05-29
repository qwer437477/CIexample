from utils.utils import Utils

from unittest import TestCase

class Testutils(TestCase):

    def setUp(self):
        self.util = Utils()
        

    def test_utils_method_add_raise_ValueError_when_given_argument_is_not_Integer(self):
        pass

    def test_utils_method_add_will_return_the_sum_of_input_arguments(self):
        sum = self.util.add(1, 2)

        self.assertEqual(sum, 3)
        