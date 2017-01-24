# # # EXCERCISE 5
# import random
#
# #########################
# class Tables(object):
#
# class Roulette(Tables):
#
#     def minbet(self):
#         self.minbet = random.choice([50,100,200])
#
# class Craps(Tables):
#     def minbet(self):
#         self.minbet = random.choice([0,25,50])

##########################
import Tables
import random
from random import randint
##########################
##########################
##########################


class Employees(object):
    def __init__(self, fixed_wage):
        self.fixed_wage = fixed_wage


class Croupiers(Employees):
    def __init__(self, fixed_wage):
        self.total_wage = fixed_wage

    def total_wage(self, profit): #profit (per table) should be defined in "tables"
        self.total_wage += Tables.profit * 0.005
        return self.total_wage

###########################


class Barmen(Employees):

    def __init__(self, fixed_wage):
        self.total_wage = fixed_wage

    def tips(self, customer):
        if customer.current_budget >= 60 :
            self.total_wage += customer.tips
        else:
            self.total_wage += 0
        return self.total_wage

#############################
#############################
#############################


class Customers(object):
    def __init__(self, initial_budget, bet, current_budget, drinks, tips):
        self.initial_budget = initial_budget
        self.bet = bet
        self.value_won = Tables.value_won
        self.current_budget = current_budget
        self.drinks = drinks
        self.tips = tips

    def current_budget(self, initial_budget, bet, gain):
        self.current_budget = initial_budget - bet + gain

    def drinks(self, current_budget):
        if current_budget >= 60 :
            self.drinks = random.choice([20,40])
        else:
            self.drinks = 0
        return self.drinks
        self.current_budget -= self.drinks

    def tips(self,current_budget):

        if current_budget >= 60:
            self.tips = randint(0,20)
        else:
            self.tips = 0
###########################


class Returning(Customers):
    def initial_budget(self):
        self.initial_budget = randint(100,300)
        return self.initial_budget

    def bet(self, minbet, initial_budget):
        if initial_budget >= Tables.mini :
            return minbet
        else:
            return 0

############################


class one_time(Customers):
    def initial_budget(self):
        self.initial_budget = randint(200, 300)

    def bet(self, initial_budget):
        self.bet = randint(0, initial_budget/3)

############################


class Bachelor(Customers):
    def initial_budget(self):
        self.initial_budget = randint(200, 500)
        return self.initial_budget

    def total_budget(self,promotion):
        self.initial_budget += promotion

    def bet(self, initial_budget):
        self.bet = randint(0, initial_budget)
        return self.bet