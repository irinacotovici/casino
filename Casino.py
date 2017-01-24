import Tables
import people


class Casino(object):
    def __init__(self, r_tables, c_tables, croupiers, barmen, customers):
        self.r_tables = r_tables  # List of roulette tables
        self.c_tables = c_tables  # List of craps tables
        self.croupiers = croupiers  # List of croupiers
        self.barmen = barmen  # List of barmen
        self.customers = customers  # List of customers

    def buy_tables(self, n_roulette, n_craps):
        self.r_tables = [Tables.Roulette(0) for i in range(n_roulette)]
        [x.set_minimum() for x in self.r_tables]
        self.c_tables = [Tables.Craps(0) for i in range(n_craps)]
        [x.set_minimum() for x in self.c_tables]

    def hire_employees(self, n_croupier):
        self.croupiers = [people.Croupier(1) for i in range(n_roulette)]
        [x.set_minimum() for x in self.r_tables]


# n_roulette = 10

# print(roulettes)
# print([x.mini for x in roulettes])

