import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.extractPL import position_histogram

'''
Number of transfers by position
'''

df = pd.DataFrame(position_histogram.values(), index=position_histogram.keys(), columns=[' '])

df.plot(kind="pie", subplots=True, figsize=(8,8), fontsize=14)
plt.gca().get_legend().remove()
plt.show()