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
        self.r_tables = [Tables.Roulette(0, [], []) for i in range(n_roulette)]
        [x.set_minimum() for x in self.r_tables]
        self.c_tables = [Tables.Craps(0, [], []) for i in range(n_craps)]
        [x.set_minimum() for x in self.c_tables]

    def hire_employees(self, n_barmen):
        n_croupier = len(self.r_tables) + len(self.c_tables)
        self.croupiers = [people.Croupiers(1) for i in range(n_croupier)]
        self.barmen = [people.Barmen(1) for i in range(n_barmen)]

    def assign_croupiers(self):
        # for x, y in zip([self.r_tables + self.c_tables], self.croupiers):
        for x, y in zip(self.r_tables + self.c_tables, self.croupiers):
            x.croupier = y

    # def open_doors(self, capacity):
    #     self.customers = [Tables.Roulette(0, [], []) for i in range(n_roulette)]


monte_carlo = Casino([], [], [], [], [])
monte_carlo.buy_tables(10, 10)
monte_carlo.hire_employees(4)
monte_carlo.assign_croupiers()
print([x.croupier for x in monte_carlo.r_tables])
print([x.croupier for x in monte_carlo.c_tables])
print(monte_carlo.croupiers)
print(monte_carlo.barmen)

# n_roulette = 10

# print(roulettes)
# print([x.mini for x in roulettes])

