
def parse_input(dial_movement):
    dial_direction = dial_movement[0]
    if dial_direction not in ('L', 'R'):
        print('--INVALID DIRECTION IN INPUT FILE--')
        exit(1)
    dial_distance = int(dial_movement[1:])
    return dial_direction, dial_distance

def spin_dial(starting_location, spin_direction, change):
    if spin_direction == 'R':
        return (starting_location + change) % 100
    elif spin_direction == 'L':
        ending_location = starting_location - change
        if ending_location == 0:
            return 0
        elif ending_location < 0:
            return 100 - abs(ending_location) % 100
        else:
            return ending_location
    return '--INVALID INPUT--'

def print_movement(change, end_location):
   print('The dial is rotated ' + change + ' to point at ' + str(end_location))

# with open('./one/input.txt', 'r') as file:
#     location = 50
#     finishing_zeroes = 0
#     for line in file:
#         direction, distance = parse_input(line)
#         location = spin_dial(location, direction, distance)
#         print_movement(line, location)
#         if location == 0:
#             finishing_zeroes += 1
#     print('YOUR ANSWER IS - ' + str(finishing_zeroes))
#
#
