import Tables
import People
import random


class Casino(object):
    def __init__(self, r_tables=[], c_tables=[], croupiers=[], barmen=[], customers=[], cash=50000, promotion=200):
        self.r_tables = r_tables  # List of roulette tables
        self.c_tables = c_tables  # List of craps tables
        self.croupiers = croupiers  # List of croupiers
        self.barmen = barmen  # List of barmen
        self.customers = customers  # List of customers
        self.cash = cash  # Starting cash of the casino
        self.promotion = promotion  # Promotion given to bachelors

    def buy_tables(self, n_roulette, n_craps):
        """Creates the tables and randomly sets their minimum bets"""
        self.r_tables = [Tables.Roulette(0, [], []) for _ in range(n_roulette)]
        [x.set_minimum() for x in self.r_tables]
        self.c_tables = [Tables.Craps(0, [], []) for _ in range(n_craps)]
        [x.set_minimum() for x in self.c_tables]

    def hire_employees(self, n_barmen=4):
        """Creates barmen and only as many croupiers as needed"""
        n_croupier = len(self.r_tables) + len(self.c_tables)
        self.croupiers = [People.Croupiers(200) for _ in range(n_croupier)]
        self.barmen = [People.Barmen(200) for _ in range(n_barmen)]

    def assign_croupiers(self):
        """Assign each croupier to a table, needs the same number of the croupiers and tables"""
        for x, y in zip(self.r_tables + self.c_tables, self.croupiers):
            x.croupier = y

    def open_doors(self, capacity=100, per_returning=.5, per_bachelors=.2):
        """Creates customers in approximately the right proportions and sets their initial budgets"""
        n_returning = round(capacity * per_returning)
        n_bachelors = round(capacity * per_bachelors)
        n_one_time = capacity - n_returning - n_bachelors
        returners = [People.Returning([], [], [], [], []) for _ in range(n_returning)]
        one_timers = [People.OneTime([], [], [], [], []) for _ in range(n_one_time)]
        bachelors = [People.Bachelor([], [], [], [], []) for _ in range(n_bachelors)]
        [x.set_initial_budget() for x in list(returners + one_timers + bachelors)]
        for x in bachelors:
            x.initial_budget += self.promotion
            self.cash -= self.promotion
        self.customers = list(returners + one_timers + bachelors)

    def get_a_drink(self):
        """Assign to every customer a barman randomly, and they buy drinks"""
        which_barmen = [random.randint(1, len(self.barmen)) for _ in self.customers]
        for x in range(len(self.customers) - 1):
            self.customers[x].barman = self.barmen[which_barmen[x]]

    def fill_tables(self):
        """Assigns every customer to a table randomly"""
        which_table = [random.randint(1, len(self.c_tables + self.r_tables)) for _ in self.customers]
        for x in range(len(self.customers)-1):
            (self.c_tables + self.r_tables)[which_table[x]-1].customers.append(self.customers[x])

    def clear_tables(self):
        """Clears the customer list of every table"""
        for x in (self.r_tables + self.c_tables):
            x.customers = []

monte_carlo = Casino([], [], [], [], [])
monte_carlo.buy_tables(10, 10)
monte_carlo.hire_employees(4)
monte_carlo.assign_croupiers()
# monte_carlo.assign_croupiers()
monte_carlo.open_doors()
print([x.croupier for x in monte_carlo.r_tables])
print([x.croupier for x in monte_carlo.c_tables])
print(monte_carlo.croupiers)
print(monte_carlo.barmen)
print(monte_carlo.customers)
print([x.initial_budget for x in monte_carlo.customers])
print(monte_carlo.cash)

# Maybe a dictionary is not needed
print("Test")
print(monte_carlo.croupiers)
print(monte_carlo.r_tables[0].croupier)
monte_carlo.croupiers[0].total_wage = 10
print(monte_carlo.r_tables[0].croupier.total_wage)
# e.g. the objects are the same

# print(monte_carlo.fill_tables())

print(range(len(monte_carlo.customers)))
print(monte_carlo.customers[99])
monte_carlo.fill_tables()

print(range(2, 12))
print(range(1, 36))
print(range(0))

print(monte_carlo.r_tables[1].bet_range)

print(random.randint(range(1, 36)))
