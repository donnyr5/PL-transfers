import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.extractPL import position_spending

'''
Average transfer fee by position
'''

df = pd.DataFrame(position_spending.values(), index=position_spending.keys(), columns=[' '])

df.plot(kind="bar", subplots=True, figsize=(8,8))
plt.title("Average transfer fee by position 2018-2023 (loans are considered free)")
plt.xlabel("Position")
plt.ylabel("Transfer Fee (€ in millions)")
plt.gca().get_legend().remove()

plt.show()