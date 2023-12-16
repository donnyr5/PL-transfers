import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.other_clubs import where_are_players_going

'''
Where are players going?
'''

values = []
clubs = []
for item in where_are_players_going:
    values.append(item[1])
    clubs.append(item[0])

df = pd.DataFrame(values, index=clubs, columns=[' '])

df.plot(kind="bar", subplots=True, figsize=(8,8))
plt.title("Where are Premier League Players Going?")
plt.xlabel("Club")
plt.ylabel("# of Departures")
plt.show()