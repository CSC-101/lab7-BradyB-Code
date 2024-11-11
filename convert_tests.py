import convert
import unittest
from convert import str_to_float


# Task 1
class ConvertTests(unittest.TestCase):
    def test_str_to_float_1(self):
        input = "34.2"
        result = convert.str_to_float(input)
        expected = 34.2
        self.assertEqual(expected, result)

    def test_str_to_float_2(self):
        input = "-2.0"
        result = convert.str_to_float(input)
        expected = -2.0
        self.assertEqual(expected, result)

    def test_str_to_float_3(self):
        input = "aa2"
        result = convert.str_to_float(input)
        expected = None
        self.assertEqual(expected, result)


if __name__ == '__main__':
        unittest.main()
