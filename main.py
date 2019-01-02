from random import randint, choice

def monty_hall(ignorant=False, iterations=100000):
    player_wins = 0
    for i in range(iterations+1):
        car_door = randint(1, 3)
        player_door = randint(1, 3)
        remaining_door = 6 - car_door - player_door
        if not ignorant:
            if player_door != car_door:  # Since the player will always switch doors
                player_wins += 1
        if ignorant:
            if player_door != car_door and choice([remaining_door, car_door]) == remaining_door:
                player_wins += 1
    return float(player_wins / iterations)

print('The player wins {:.1%} in the classic Monty Hall problem and {:.1%} of the time in the ignorant Monty hall problem.'.format(monty_hall(), monty_hall(ignorant=True)))
