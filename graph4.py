import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.extractPL import position_histogram

df = pd.DataFrame(position_histogram.values(), index=position_histogram.keys(), columns=[' '])

df.plot(kind="pie", subplots=True, figsize=(8,8))
plt.legend(['Legend'], loc='upper left')

plt.show()