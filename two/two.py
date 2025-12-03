location = 50
finishing_zeroes = 0
with open('../one/input.txt') as file:
    for line in file:
        dial_direction = line[0]
        dial_distance = int(line[1:])
        if dial_direction == 'R':
            overflow_location = (location + dial_distance)
            if overflow_location > 100:
                finishing_zeroes += (1 * (overflow_location // 100))
            location = overflow_location % 100
        else:
            overflow_location = location - dial_distance
            if overflow_location < 0 and location != 0:
                finishing_zeroes += abs(1 * overflow_location // 100)
            location = overflow_location % 100
        if location == 0:
            finishing_zeroes += 1
        print(dial_direction + ' '+ str(dial_distance) + ' '+ str(location))
        print(finishing_zeroes)
    print(finishing_zeroes)


#3420
#6102

