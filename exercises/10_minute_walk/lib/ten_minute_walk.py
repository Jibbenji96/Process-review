

def ten_minute_walk(route_array):
    compass = {'n': 1, 's': -1, 'e': 1, 'w': -1}
    score = 0
    if len(route_array) == 10:
        for direction in route_array:
            number = compass[direction]
            score += number
        if score == 0:
                return True
    return False