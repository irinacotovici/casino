import Roulette
from random import randint


class Craps(Roulette.Table):
    """Defines a roulette table"""
    def __init__(self, mini):
        Roulette.Table.__init__(self, mini)

    def dices(self, n=2):
        """Rolls n dices and gives their sum"""
        sum_dices = 0
        for i in range(n):
            sum_dices += randint(1, 6)
        return sum_dices

    def roll_the_dices(self, bet_on, n=2):
        """Rolls the dices and tells which players won (not accounting for minimum bet)"""
        draw = self.dices(n)
        wins = [bet == draw for bet in bet_on]
        print("Dices sum to " + str(draw))
        if not any(wins):
            print("No player won")
        else:
            players = [i for i, x in enumerate(wins) if x]
            print("Players " + str(players) + " won")
        return wins

    def calculate_prize(self, bet_on, expected_return=0.9):
        """Calculates the prize for a correct bet based on the sum of two dices and a expected return of 90%"""
        prob = 6 - abs(bet_on - 7)/6
        prize = expected_return/prob
        return prize

    def simulate_game(self, bets, bet_on, n=2, expected_return=0.9):
        """Simulates a round of Craps, gives the amounts won by each player and the casino's profit"""
        above_list = self.above_minimum(bets)
        wins = self.roll_the_dices(bet_on, n)
        value_won = [round(above * win * bet * self.calculate_prize(on, expected_return)) for
                     win, bet, above, on in zip(wins, bets, above_list, bet_on)]
        profit = sum(bets) - sum(value_won)
        return [value_won, profit]
