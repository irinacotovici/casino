
##########################
import random
from random import randint
###########################


class Employees(object):
    def __init__(self, fixed_wage):
        self.total_wage = fixed_wage


class Croupiers(Employees):
        def total_wage(self, fixed_wage, profit):
            self.total_wage = fixed_wage
            self.total_wage += profit * 0.005
            return self.total_wage

###########################


class Barmen(Employees):

    # def __init__(self, fixed_wage, drinks, tips):
    #     self.total_wage = fixed_wage
    #     self.drinks = drinks
    #     self.tips = tips

    def adjusted_wage(self, tips):
        self.total_wage += tips

    # def drinks_served(self, drinks):
    #     self.drinks += drinks
    #
    # def tips_received(self, tips):
    #     self.tips += tips

#############################
#############################
#############################


class Customers(object):
    def __init__(self, bet, current_budget, drinks, tips, gain, barman):
        self.bet = bet
        self.gain = gain
        self.current_budget = current_budget
        self.drinks = drinks
        self.tips = tips
        self.barman = barman

    def current_budget(self, bet, gain):
        self.current_budget -= bet
        self.current_budget += gain

    def drinks(self, current_budget):
        if current_budget >= 60:
            self.drinks = random.choice([20, 40])
        else:
            self.drinks = 0

        self.current_budget -= self.drinks

    def tips(self, current_budget):
        if current_budget >= 20:
            self.tips = randint(0, 20)
        else:
            self.tips = 0

        self.current_budget -= self.tips

###########################


class Returning(Customers):
    def initial_budget(self):
        self.current_budget = randint(100, 300)
        return self.current_budget

    def bet(self, min_bet, current_budget):
        if current_budget >= min_bet:
            return min_bet
        else:
            return 0

############################


class OneTime (Customers):
    def initial_budget(self):
        self.current_budget = randint(200, 300)

    def bet(self, current_budget):
        self.bet = randint(0, current_budget/3)

############################


class Bachelor(Customers):
    def initial_budget(self):
        self.current_budget = randint(200, 500)
        return self.current_budget

    def total_budget(self, promotion):
        self.current_budget += promotion

    def bet(self, current_budget):
        self.bet = randint(0, current_budget)
        return self.bet
