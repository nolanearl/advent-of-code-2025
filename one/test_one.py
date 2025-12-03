import unittest

from one.one import DayOne

class Test(unittest.TestCase):
    def test_parse_input_happy_path(self):
        day_one= DayOne()
        self.assertEqual(('L', 100), day_one.parse_input("L100"))

    def test_parse_input_invalid_direction(self):
        day_one = DayOne()
        with self.assertRaises(SystemExit) as ec:
            day_one.parse_input("S100")
            self.assertEqual(1, ec.exception.code)

    def test_parse_input_no_direction(self):
        day_one = DayOne()
        with self.assertRaises(SystemExit) as ec:
            day_one.parse_input("100")
            self.assertEqual(1, ec.exception.code)

    def test_spin_dial_right_no_overflow(self):
        day_one = DayOne()
        result = day_one.spin_dial(20, 'R', 13)
        self.assertEqual(33, result)

    def test_spin_dial_right_overflow(self):
        day_one = DayOne()
        result = day_one.spin_dial(99, 'R', 13)
        self.assertEqual(12, result)

    def test_spin_dial_right_large_overflow(self):
        day_one = DayOne()
        result = day_one.spin_dial(99, 'R', 313)
        self.assertEqual(12, result)

    def test_spin_dial_left_no_overflow(self):
        day_one = DayOne()
        result = day_one.spin_dial(99, 'L', 13)
        self.assertEqual(86, result)

    def test_spin_dial_left_overflow(self):
        day_one = DayOne()
        result = day_one.spin_dial(0, 'L', 13)
        self.assertEqual(87, result)

    def test_spin_dial_left_large_overflow(self):
        day_one = DayOne()
        result = day_one.spin_dial(0, 'L', 213)
        self.assertEqual(87, result)

    def test_spin_dial_left_zero(self):
        day_one = DayOne()
        result = day_one.spin_dial(1, 'L', 1)
        self.assertEqual(0, result)

    def test_example(self):
        day_one = DayOne()
        finishing_zeroes = 0
        current_location = 50
        with open('./one/example.txt', 'r') as file:
            for line in file:
                instruction, expected_result = line.split('-')
                direction, distance = day_one.parse_input(instruction)
                current_location = day_one.spin_dial(current_location, direction, distance)
                if current_location == 0:
                    finishing_zeroes += 1
                self.assertEqual(int(expected_result), current_location)
                print(instruction+'-'+str(current_location))
        self.assertEqual(finishing_zeroes, 3)
        print('YOUR ANSWER IS - ' + str(finishing_zeroes))





