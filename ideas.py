import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

'''
1. Spending = domestic success?
X axis: average spending last (2,5,10) years
Y axis: average league position
Note: A team must be in the league > 2 seasons to be included

2. What about other trophies?
Lets take the top 20 biggest spenders from the previous graph and compare their total trophy count in last 10 years

'''
s = pd.Series([1, 3, 5, np.nan, 6, 8])
print(s)

dates = pd.date_range("20130101", periods=6)

print(dates)

df = pd.DataFrame(np.random.randn(6, 4), index=dates, columns=list("ABCD"))
print(df)

df2 = pd.DataFrame(
    {
        "A": 1.0,
        "B": pd.Timestamp("20130102"),
        "C": pd.Series(1, index=list(range(4)), dtype="float32"),
        "D": np.array([3] * 4, dtype="int32"),
        "E": pd.Categorical(["test", "train", "test", "train"]),
        "F": "foo",
    }
)
print(df2)


# Data for plotting
x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]

plt.plot(x, y) # Plotting the data
plt.xlabel('X axis label') # X-axis label
plt.ylabel('Y axis label') # Y-axis label
plt.title('Basic Graph using Matplotlib') # Graph title
plt.grid(True) # Show grid
plt.show() # Display the graph

'''
make Dataframe with all info we have processed for each team. 
- each time will have own entry:
    - average net spending last 10 years
    - average goal differential in league
    - average position in the table leage
    for now..
'''

