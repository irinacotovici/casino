import Tables
import People


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
        self.r_tables = [Tables.Roulette(0, [], []) for i in range(n_roulette)]
        [x.set_minimum() for x in self.r_tables]
        self.c_tables = [Tables.Craps(0, [], []) for i in range(n_craps)]
        [x.set_minimum() for x in self.c_tables]

    def hire_employees(self, n_barmen=4):
        """Creates barmen and only as many croupiers as needed"""
        n_croupier = len(self.r_tables) + len(self.c_tables)
        self.croupiers = [People.Croupiers(200) for i in range(n_croupier)]
        self.barmen = [People.Barmen(200) for i in range(n_barmen)]

    def assign_croupiers(self):
        """Assign each croupier to a table, needs the same number of the croupiers and tables"""
        for x, y in zip(self.r_tables + self.c_tables, self.croupiers):
            x.croupier = y

    def open_doors(self, capacity=100, per_returning=.5, per_bachelors=.2):
        """Creates customers in approximately the right proportions and sets their initial budgets"""
        n_returning = round(capacity * per_returning)
        n_bachelors = round(capacity * per_bachelors)
        n_one_time = capacity - n_returning - n_bachelors
        returners = [People.Returning([], [], [], [], []) for i in range(n_returning)]
        one_timers = [People.OneTime([], [], [], [], []) for i in range(n_one_time)]
        bachelors = [People.Bachelor([], [], [], [], []) for i in range(n_bachelors)]
        [x.set_initial_budget() for x in list(returners + one_timers + bachelors)]
        for x in bachelors:
            x.initial_budget += self.promotion
            self.cash -= self.promotion
        self.customers = list(returners + one_timers + bachelors)

monte_carlo = Casino([], [], [], [], [])
monte_carlo.buy_tables(10, 10)
monte_carlo.hire_employees(4)
monte_carlo.assign_croupiers()
monte_carlo.assign_croupiers()
monte_carlo.open_doors()
print([x.croupier for x in monte_carlo.r_tables])
print([x.croupier for x in monte_carlo.c_tables])
print(monte_carlo.croupiers)
print(monte_carlo.barmen)
print(monte_carlo.customers)
print([x.initial_budget for x in monte_carlo.customers])
print(monte_carlo.cash)

# Maybe a dictionary is not needed
print(monte_carlo.croupiers)
print(monte_carlo.r_tables[0].croupier)
monte_carlo.croupiers[0].total_wage = 10
print(monte_carlo.r_tables[0].croupier.total_wage)
# e.g. the objects are the same

