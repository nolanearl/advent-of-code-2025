import unittest
from one import one


class Test(unittest.TestCase):

    def test_parse_input_happy_path(self):
        self.assertEqual(('L', 100), one.parse_input("L100"))

    def test_parse_input_invalid_direction(self):
        with self.assertRaises(SystemExit) as ec:
            one.parse_input("S100")
            self.assertEqual(1, ec.exception.code)

    def test_parse_input_no_direction(self):
        with self.assertRaises(SystemExit) as ec:
            one.parse_input("100")
            self.assertEqual(1, ec.exception.code)

    def test_spin_dial_right_no_overflow(self):
        result = one.spin_dial(20, 'R', 13)
        self.assertEqual(33, result)

    def test_spin_dial_right_overflow(self):
        result = one.spin_dial(99, 'R', 13)
        self.assertEqual(12, result)

    def test_spin_dial_right_large_overflow(self):
        result = one.spin_dial(99, 'R', 313)
        self.assertEqual(12, result)

    def test_spin_dial_left_no_overflow(self):
        result = one.spin_dial(99, 'L', 13)
        self.assertEqual(86, result)

    def test_spin_dial_left_overflow(self):
        result = one.spin_dial(0, 'L', 13)
        self.assertEqual(87, result)

    def test_spin_dial_left_large_overflow(self):
        result = one.spin_dial(0, 'L', 213)
        self.assertEqual(87, result)

    def test_spin_dial_left_zero(self):
        result = one.spin_dial(1, 'L', 1)
        self.assertEqual(0, result)


