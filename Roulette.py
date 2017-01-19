import random
# This is used to fix the random number generator so we can test the output
random.seed(3456)

for i in range(1, 6):
    print(random.randint(1, 10))
# 7, 8, 5, 3, 9: OK

# Function AboveMinimum


def above_minimum(bets, mini):
    """ Checks if the bets are above the minimum of the table """
    above = [bet >= mini for bet in bets]
    return above

print(above_minimum([1, 2, 4, 5], 2))
# test OK


def spin_the_wheel(bets):
    draw = random.randint(0, 36)
    wins = [bet == draw for bet in bets]
    if not any(wins):
        print("No player won")
    print(draw)
    return wins

print(spin_the_wheel([2, 8, 9, 26, 14]))
print(spin_the_wheel([2, 8, 9, 26, 14]))
# Tests OK
