"""Defines functions related to the roulette game"""
import random

# This is used to fix the random number generator so we can test the output
random.seed(3456)


class Table(object):
    """Defines a table"""
    def __init__(self, mini):
        self.mini = mini

    def above_minimum(self, bets):
        """ Checks if the bets are above the minimum of the table """
        above = [bet >= self.mini for bet in bets]
        return above

class Roulette(Table):
    """Defines a roulette table"""
    def __init__(self, mini):
        Table.__init__(self, mini)

    def spin_the_wheel(self, bet_on):
        """Spins the wheel and tells which players won (not accounting for minimum bet)"""
        draw = random.randint(0, 36)
        wins = [bet == draw for bet in bet_on]
        if not any(wins):
            print("No player won")
        print("Ball lands on " + str(draw))
        return wins

    def simulate_game(self, bets, bet_on):
        """Simulates a round of roulette, gives the amounts won by each player and the casino's profit"""
        above_list = self.above_minimum(bets)
        wins = self.spin_the_wheel(bet_on)
        value_won = [above * win * bet * 30 for win, bet, above in zip(wins, bets, above_list)]
        profit = sum(bets) - sum(value_won)
        return [value_won, profit]
