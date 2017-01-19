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
