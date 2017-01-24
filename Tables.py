"""Defines classes for tables and games"""
import random


class Table(object):
    """Defines a table"""
    def __init__(self, mini, croupier, customers):
        self.mini = mini
        self.croupier = croupier
        self.croupier = customers

    def above_minimum(self, bets):
        """ Checks if the bets are above the minimum of the table """
        above = [bet >= self.mini for bet in bets]
        return above


class Roulette(Table):
    """Defines a roulette table"""
    # def __init__(self, mini):
    #     Table.__init__(self, mini)

    def set_minimum(self):
        self.mini = random.choice([50, 100, 200])

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


class Craps(Table):
    """Defines a roulette table"""
    # def __init__(self, mini):
    #     Table.__init__(self, mini)

    def set_minimum(self):
        self.mini = random.choice([0, 25, 50])

    def dices(self, n=2):
        """Rolls n dices and gives their sum"""
        sum_dices = 0
        for i in range(n):
            sum_dices += random.randint(1, 6)
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
        prob = (6 - abs(bet_on - 7))/36
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
