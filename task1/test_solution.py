import unittest

from task1.solution import strict


@strict
def test_sum_two(a: int, b: int) -> int:
    return a + b


class StrictDecoratorTest(unittest.TestCase):
    def test_correct_case(self):
        self.assertEqual(test_sum_two(1, 2), 3)


    def test_invalid_float_arg_type(self):
        with self.assertRaises(TypeError):
            test_sum_two(1, 2.0)


    def test_invalid_float_kwarg_type(self):
        with self.assertRaises(TypeError):
            test_sum_two(1, b=2.0)


    def test_invalid_str_arg_type(self):
        with self.assertRaises(TypeError):
            test_sum_two('1', 2)


if __name__ == '__main__':
    unittest.main()
