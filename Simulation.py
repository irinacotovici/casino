import Roulette
import Craps
from collections import Counter
import numpy as np
from matplotlib import pyplot as plt

amounts1 = [10, 85, 120, 65, 150, 122]
bets1 = [10, 24, 36, 0, 11, 24]
table1 = Roulette.Roulette(100)
print(table1.simulate_game(amounts1, bets1))
print(table1.simulate_game(amounts1, bets1))

amounts2 = [10, 85, 120, 65, 150, 122]
bets2 = [10, 12, 6, 2, 11, 5]
table2 = Craps.Craps(100)
print(table2.simulate_game(amounts2, bets2))
print(table2.simulate_game(amounts2, bets2))

# Create 1000 simulations of the craps game:

result_profit = []
result_value_won = []
dices = []
for i in range(1000):
    result = table2.simulate_game(amounts2, bets2)
    result_value_won.append(result[0])
    result_profit.append(result[1])
    dices.append(table2.dices())
print(result_value_won)
print(result_profit)
print(dices)

thousandsthrows = dices

labels, values = zip(*Counter(thousandsthrows).items())
indexes = np.arange(len(labels))
width = 1
plt.bar(indexes, values, width)
plt.xticks(indexes + width * 0.5, labels)
plt.show()