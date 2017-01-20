"""Defines functions related to the roulette game"""
import random


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
        print("Ball lands on " + str(draw))
        if not any(wins):
            print("No player won")
        else:
            players = [i for i, x in enumerate(wins) if x]
            print("Players " + str(players) + " won")
        return wins

    def simulate_game(self, bets, bet_on):
        """Simulates a round of roulette, gives the amounts won by each player and the casino's profit"""
        above_list = self.above_minimum(bets)
        wins = self.spin_the_wheel(bet_on)
        value_won = [above * win * bet * 30 for win, bet, above in zip(wins, bets, above_list)]
        profit = sum(bets) - sum(value_won)
        return [value_won, profit]
