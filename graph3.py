import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from abrev import team_abbreviations
from data.detailed_transfers.extractPL import avg_age
from data.league_tables.process_tables import avg_pts_5_seasons

'''
Average points per season vs. average age of transfer in 18-23.
'''

# (average age, points total) for each team.
ages_points = {}
for team in avg_pts_5_seasons:
    if (team == "Cardiff City") or (team == "West Bromwich Albion"):
         continue
    
    if (avg_age[team] is not None):
        if (avg_age[team] > 26):
             print(team)
        ages_points[team] = (avg_age[team], avg_pts_5_seasons[team] )

x_points = []
for data in ages_points.values():
     x_points.append(data[0])
y_points = []
for data in ages_points.values():
     y_points.append(data[1])

plt.scatter(x_points,y_points)

for team_name, data in ages_points.items():
     if (team_name == "Newcastle United") or (team_name == "AFC Bournemouth"):
          plt.annotate(team_abbreviations[team_name],  # this is the text
                    data,  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(-15,-5),  # distance from text to points (x,y)
                    ha='center')  # horizontal alignment can be left, right or center
     else:
          plt.annotate(team_abbreviations[team_name],  # this is the text
                    data,  # these are the coordinates to position the label
                    textcoords="offset points",  # how to position the text
                    xytext=(0,5),  # distance from text to points (x,y)
                    ha='center')  # horizontal alignment can be left, right or center

# Set the title and labels for the axes
plt.title('Average Points per Season vs. Average age of Transfer in 2017/18 - 2022/23')
plt.xlabel('Average Age of incoming Transfer')
plt.ylabel('Average Points per Season')

# Calculate coefficients for the line of best fit
b, a = np.polyfit(x_points, y_points, deg=1)
# Create a polynomial function from the coefficients
line_of_best_fit = np.poly1d((b, a))
print("For every year younger the average age, ", b, " points are gained throughout the season.")
# Generate y-values for each x-value using the line of best fit
plt.plot(x_points, line_of_best_fit(x_points), color='green')

plt.show()
