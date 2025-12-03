
class DayOne:
    @staticmethod
    def parse_input(dial_movement):
        dial_direction = dial_movement[0]
        if dial_direction not in ('L', 'R'):
            print('--INVALID DIRECTION IN INPUT FILE--')
            exit(1)
        dial_distance = int(dial_movement[1:])
        return dial_direction, dial_distance

    @staticmethod
    def spin_dial(location, spin_direction, change):
        if spin_direction == 'R':
            return (location + change) % 100
        elif spin_direction == 'L':
            return (location - change) % 100
        return '--INVALID INPUT--'

    @staticmethod
    def print_movement(change, end_location):
       print('The dial is rotated ' + change + ' to point at ' + str(end_location))

    def __init__(self):
        self.current_location= 50
        self.finishing_zeroes = 0
        with open('./one/input.txt', 'r') as file:
            for line in file:
                direction, distance = self.parse_input(line)
                self.current_location = self.spin_dial(self.current_location, direction, distance)
                self.print_movement(line, self.current_location)
                if self.current_location== 0:
                    self.finishing_zeroes += 1
            print('YOUR ANSWER IS - ' + str(self.finishing_zeroes))

if __name__ == '__main__':
    one = DayOne()
