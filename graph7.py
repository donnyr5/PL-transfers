import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.other_clubs import where_are_players_coming_from

'''
Where are players Coming from?
'''

values = []
clubs = []
for item in where_are_players_coming_from:
    values.append(item[1])
    clubs.append(item[0])

df = pd.DataFrame(values, index=clubs, columns=[' '])

df.plot(kind="bar", subplots=True, figsize=(8,8))
plt.title("Where are Premier League Players Coming From?")
plt.xlabel("Club")
plt.ylabel("# of Arrivals")
plt.show()